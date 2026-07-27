import CDP from 'chrome-remote-interface';

let client = null;
let targetInfo = null;
const CDP_HOST = 'localhost';
const CDP_PORT = 9222;
const MAX_RETRIES = 5;
const BASE_DELAY = 500;

// Known direct API paths discovered via live probing (see PROBE_RESULTS.md)
const KNOWN_PATHS = {
  chartApi: 'window.TradingViewApi._activeChartWidgetWV.value()',
  chartWidgetCollection: 'window.TradingViewApi._chartWidgetCollection',
  bottomWidgetBar: 'window.TradingView.bottomWidgetBar',
  replayApi: 'window.TradingViewApi._replayApi',
  alertService: 'window.TradingViewApi._alertService',
  chartApiInstance: 'window.ChartApiInstance',
  mainSeriesBars: 'window.TradingViewApi._activeChartWidgetWV.value()._chartWidget.model().mainSeries().bars()',
  // Phase 1: Strategy data — model().dataSources() → find strategy → .performance().value(), .ordersData(), .reportData()
  strategyStudy: 'chart._chartWidget.model().model().dataSources()',
  // Phase 2: Layouts — getSavedCharts(cb), loadChartFromServer(id)
  layoutManager: 'window.TradingViewApi.getSavedCharts',
  // Phase 5: Symbol search — searchSymbols(query) returns Promise
  symbolSearchApi: 'window.TradingViewApi.searchSymbols',
  // Phase 6: Pine scripts — REST API at pine-facade.tradingview.com/pine-facade/list/?filter=saved
  pineFacadeApi: 'https://pine-facade.tradingview.com/pine-facade',
};

export { KNOWN_PATHS };

/**
 * Sanitize a string for safe interpolation into JavaScript code evaluated via CDP.
 * Uses JSON.stringify to produce a properly escaped JS string literal (with quotes).
 * Prevents injection via quotes, backticks, template literals, or control chars.
 */
export function safeString(str) {
  return JSON.stringify(String(str));
}

/**
 * Validate that a value is a finite number. Throws if NaN, Infinity, or non-numeric.
 * Prevents corrupt values from reaching TradingView APIs that persist to cloud state.
 */
export function requireFinite(value, name) {
  const n = Number(value);
  if (!Number.isFinite(n)) throw new Error(`${name} must be a finite number, got: ${value}`);
  return n;
}

export async function getClient() {
  if (client) {
    try {
      // Quick liveness check
      await client.Runtime.evaluate({ expression: '1', returnByValue: true });
      return client;
    } catch {
      client = null;
      targetInfo = null;
    }
  }
  return connect();
}

export async function connect() {
  let lastError;
  for (let attempt = 0; attempt < MAX_RETRIES; attempt++) {
    try {
      const target = await findChartTarget();
      if (!target) {
        throw new Error('No TradingView chart target found. Is TradingView open with a chart?');
      }
      targetInfo = target;
      client = await CDP({ host: CDP_HOST, port: CDP_PORT, target: target.id });

      // Enable required domains
      await client.Runtime.enable();
      await client.Page.enable();
      await client.DOM.enable();

      return client;
    } catch (err) {
      lastError = err;
      const delay = Math.min(BASE_DELAY * Math.pow(2, attempt), 30000);
      await new Promise(r => setTimeout(r, delay));
    }
  }
  throw new Error(`CDP connection failed after ${MAX_RETRIES} attempts: ${lastError?.message}`);
}

/**
 * Pick the real chart page out of a CDP /json/list response.
 *
 * WHY THIS IS FUSSY (2026-07-27): the old rule was "first page whose URL matches
 * /tradingview/i". That was written for the browser/PWA setup. Omar is now on the
 * TradingView Desktop (Store) build, which exposes several INTERNAL helper windows
 * as file:/// URLs under
 *   file:///C:/Program Files/WindowsApps/TradingView.Desktop_<ver>_.../index.html
 * The path contains "TradingView.Desktop", so the loose regex matched them. Those
 * windows have no window.TradingViewApi at all, so everything downstream dies with
 * "Cannot read properties of undefined (reading '_activeChartWidgetWV')".
 *
 * That is exactly what stranded the MCP server on the morning of 2026-07-27, and it
 * is a live risk for the nightly chain: if the chart tab is a few seconds slow, the
 * sweep binds to a helper window and the whole run fails.
 *
 * Rule now: only real http(s) pages on a tradingview.com host qualify at all, and a
 * /chart/ path wins over any other tradingview.com page. file:// is never eligible.
 *
 * Pure function so it can be unit-tested without a live browser.
 */
export function pickChartTarget(targets) {
  const pages = (targets || []).filter(t => {
    if (!t || t.type !== 'page' || typeof t.url !== 'string' || !t.url) return false;
    if (!/^https?:\/\//i.test(t.url)) return false;   // kills file:// helper windows
    try {
      return /(^|\.)tradingview\.com$/i.test(new URL(t.url).hostname);
    } catch {
      return false;
    }
  });
  const isChart = (t) => {
    try { return /^\/chart(\/|$)/i.test(new URL(t.url).pathname); }
    catch { return false; }
  };
  return pages.find(isChart) || pages[0] || null;
}

async function findChartTarget() {
  const resp = await fetch(`http://${CDP_HOST}:${CDP_PORT}/json/list`);
  const targets = await resp.json();
  return pickChartTarget(targets);
}

/**
 * Block until a real chart page exists (or timeout). Used by long unattended jobs
 * (the nightly sweep) so a slow-loading chart is waited out instead of turning into
 * a false "chain failed". Returns the target, or throws on timeout.
 */
export async function waitForChartTarget(timeoutMs = 120000, pollMs = 3000) {
  const deadline = Date.now() + timeoutMs;
  let last = null;
  for (;;) {
    try {
      const t = await findChartTarget();
      if (t) return t;
      last = 'no tradingview.com chart page among CDP targets';
    } catch (e) {
      last = e.message;
    }
    if (Date.now() >= deadline) {
      throw new Error(`No TradingView chart page after ${Math.round(timeoutMs / 1000)}s (${last}). `
        + 'Is a chart tab actually open? Desktop-app helper windows do not count.');
    }
    await new Promise(r => setTimeout(r, pollMs));
  }
}

export async function getTargetInfo() {
  if (!targetInfo) {
    await getClient();
  }
  return targetInfo;
}

export async function evaluate(expression, opts = {}) {
  const c = await getClient();
  const result = await c.Runtime.evaluate({
    expression,
    returnByValue: true,
    awaitPromise: opts.awaitPromise ?? false,
    ...opts,
  });
  if (result.exceptionDetails) {
    const msg = result.exceptionDetails.exception?.description
      || result.exceptionDetails.text
      || 'Unknown evaluation error';
    throw new Error(`JS evaluation error: ${msg}`);
  }
  return result.result?.value;
}

export async function evaluateAsync(expression) {
  return evaluate(expression, { awaitPromise: true });
}

export async function disconnect() {
  if (client) {
    try { await client.close(); } catch {}
    client = null;
    targetInfo = null;
  }
}

// --- Direct API path helpers ---
// Each returns the STRING expression path after verifying it exists.
// Callers use the returned string in their own evaluate() calls.

async function verifyAndReturn(path, name) {
  const exists = await evaluate(`typeof (${path}) !== 'undefined' && (${path}) !== null`);
  if (!exists) {
    throw new Error(`${name} not available at ${path}`);
  }
  return path;
}

export async function getChartApi() {
  return verifyAndReturn(KNOWN_PATHS.chartApi, 'Chart API');
}

export async function getChartCollection() {
  return verifyAndReturn(KNOWN_PATHS.chartWidgetCollection, 'Chart Widget Collection');
}

export async function getBottomBar() {
  return verifyAndReturn(KNOWN_PATHS.bottomWidgetBar, 'Bottom Widget Bar');
}

export async function getReplayApi() {
  return verifyAndReturn(KNOWN_PATHS.replayApi, 'Replay API');
}

export async function getMainSeriesBars() {
  return verifyAndReturn(KNOWN_PATHS.mainSeriesBars, 'Main Series Bars');
}
