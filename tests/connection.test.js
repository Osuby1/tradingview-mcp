/* Pins the CDP target-picking rule.
 *
 * WHY: on 2026-07-27 the MCP server bound itself to a TradingView Desktop helper
 * window (a file:/// page under ...WindowsApps/TradingView.Desktop_.../index.html)
 * because the old rule was "first page whose URL matches /tradingview/i" and that
 * file PATH contains "TradingView.Desktop". Helper windows have no TradingViewApi,
 * so every read failed with "_activeChartWidgetWV undefined". The same race could
 * kill the nightly sweep, which is a hard-fail step after a 40-minute scan.
 *
 * These tests are cheap and run as EOD chain step 0 alongside the Python suite.
 */
import { test } from 'node:test';
import assert from 'node:assert';
import { pickChartTarget } from '../src/connection.js';

const CHART = {
  type: 'page', id: 'chart1',
  url: 'https://www.tradingview.com/chart/QhK0cjGa/',
};
// Verbatim shapes seen in /json/list on 2026-07-27 (Store build 3.3.0.7992).
const HELPER = {
  type: 'page', id: 'helper1',
  url: 'file:///C:/Program%20Files/WindowsApps/TradingView.Desktop_3.3.0.7992_x64__n534cwy3pjxzj/resources/app.asar/app/browser-api-container/index.html',
};
const HELPER2 = {
  type: 'page', id: 'helper2',
  url: 'file:///C:/Program%20Files/WindowsApps/TradingView.Desktop_3.3.0.7992_x64__n534cwy3pjxzj/resources/app.asar/app/tabbed-window/index.html',
};
const BLANK = { type: 'page', id: 'blank', url: '' };
const WORKER = { type: 'worker', id: 'w1', url: 'https://www.tradingview.com/chart/QhK0cjGa/' };

test('picks the chart page even when helper windows are listed first', () => {
  assert.strictEqual(pickChartTarget([HELPER, HELPER2, BLANK, CHART]).id, 'chart1');
});

test('NEVER picks a file:// desktop helper window, even as the only candidate', () => {
  assert.strictEqual(pickChartTarget([HELPER, HELPER2, BLANK]), null);
});

test('ignores non-page targets such as workers', () => {
  assert.strictEqual(pickChartTarget([WORKER]), null);
});

test('prefers a /chart/ page over another tradingview.com page', () => {
  const news = { type: 'page', id: 'news', url: 'https://www.tradingview.com/news/' };
  assert.strictEqual(pickChartTarget([news, CHART]).id, 'chart1');
});

test('falls back to another tradingview.com page when no chart is open', () => {
  const news = { type: 'page', id: 'news', url: 'https://www.tradingview.com/news/' };
  assert.strictEqual(pickChartTarget([HELPER, news]).id, 'news');
});

test('rejects lookalike hosts that merely contain tradingview.com', () => {
  const evil = { type: 'page', id: 'evil', url: 'https://tradingview.com.example.net/chart/x/' };
  assert.strictEqual(pickChartTarget([evil]), null);
});

test('accepts a subdomain of tradingview.com', () => {
  const sub = { type: 'page', id: 'sub', url: 'https://in.tradingview.com/chart/AbC/' };
  assert.strictEqual(pickChartTarget([sub]).id, 'sub');
});

test('survives junk input without throwing', () => {
  assert.strictEqual(pickChartTarget(null), null);
  assert.strictEqual(pickChartTarget([]), null);
  assert.strictEqual(pickChartTarget([null, undefined, {}, { type: 'page' }]), null);
  assert.strictEqual(pickChartTarget([{ type: 'page', url: 'not a url' }]), null);
});
