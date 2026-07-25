/* O.G Chandelier universe sweep - in-page runner.
 *
 * Paste the whole file into mcp__tradingview__ui_evaluate to install, then:
 *     window.__ogSweep(SYMBOLS, 'heikinashi-2026-07-23')
 * and poll:
 *     JSON.stringify({done: window.__og.done, idx: window.__og.idx})
 *
 * Driving setSymbol in-page is ~10x cheaper than one MCP round-trip per symbol
 * (156 names in ~12 min vs ~470 tool calls).
 *
 * ---------------------------------------------------------------------------
 * STALENESS TRAP - the reason this file exists.
 * ---------------------------------------------------------------------------
 * On 2026-07-22 two full sweeps returned PLAUSIBLE BUT WRONG data: each symbol
 * carried the PREVIOUS symbol's readings under the new symbol's name. BHP came
 * back at $2.93 (BigBear.ai's price) and SMCI came back with SKYY's flip date.
 *
 * Cause: both cw.getSymbol() AND mainSeries().symbolInfo() update as soon as
 * setSymbol is called - BEFORE the bars and studies recompute. The old symbol's
 * study values are still present and still valid-looking, so any naive
 * "is it loaded yet" check passes instantly on stale data.
 *
 * A read is only trustworthy when ALL of these hold:
 *   1. mainSeries().symbolInfo().name matches the requested ticker
 *   2. every study value is non-null and bar_count > 60
 *   3. the study-value fingerprint DIFFERS from the previous symbol's
 *      (fingerprint must exclude symbol identity, or it changes too early)
 *   4. two CONSECUTIVE reads return the identical fingerprint (settled)
 *
 * Always spot-check a finished sweep against 2-3 prices you already know
 * before trusting any of it.
 *
 * ---------------------------------------------------------------------------
 * CHART TYPE - Omar's standing decision UPDATED 2026-07-23: HEIKIN ASHI.
 * ---------------------------------------------------------------------------
 * (Reverses the 2026-07-22 candles-only decision - Omar flipped the WHOLE
 * pipeline to Heikin Ashi on 2026-07-23.) Heikin Ashi and candles are not
 * interchangeable: measured across 155 names at the same instant, BUY/SELL mode
 * disagreed on 22%, flip date on 72%, and the Magical (CCI-20) reading differed
 * by a median of 14 points - enough to flip the +/-100 overbought gate on GDX,
 * NVDA and SMCI. IMPORTANT: this HA switch is for the live O.G SIGNAL read only.
 * BACKTESTS still use NORMAL candles - HA inflates backtests; see
 * research/quant-backtest-protocol.md and do not conflate the two.
 *
 * __ogSweep REFUSES to run on any style but Heikin Ashi unless you pass
 * allowOtherStyle=true, and every result row records the style it was read on.
 */
(function () {
  var STYLE_NAMES = {0:'Bars',1:'Candles',2:'Line',3:'Area',4:'Renko',5:'Kagi',
                     6:'PnF',7:'LineBreak',8:'HeikinAshi',9:'HollowCandles'};

  function widget() {
    return window.TradingViewApi._activeChartWidgetWV.value()._chartWidget;
  }

  // Rounding helper, hoisted to module scope 2026-07-25. It used to live inside
  // __ogRead only, so the quote-retry loop in __ogSweep threw ReferenceError on
  // every attempt - and the retry's own catch swallowed it silently, 25 times
  // per name. The symptom looked exactly like "the quote never arrived".
  function f(x) {
    return (x == null || (typeof x === 'number' && isNaN(x)))
      ? null : Math.round(x * 10000) / 10000;
  }

  function chartStyle() {
    try { return widget().model().model().mainSeries().properties().style.value(); }
    catch (e) { return null; }
  }

  window.__ogRead = function () {
    var cw = widget();
    var sources = cw.model().model().dataSources();
    var r = {};

    for (var i = 0; i < sources.length; i++) {
      var mi = null;
      try { mi = sources[i].metaInfo ? sources[i].metaInfo() : null; } catch (e) {}
      if (!mi) continue;
      var d = null;
      try { d = sources[i].data(); } catch (e) { continue; }
      if (!d || !d.lastIndex) continue;
      var end = d.lastIndex();
      if (end == null) continue;

      if (mi.description === 'Chandelier Exit') {
        var lastV = d.valueAt(end);
        if (!lastV) continue;
        // plot order: [time, LongStop, LongStopStart, BuyLabel, ShortStop,
        //              ShortStopStart, SellLabel, ...]
        r.ce_mode = (lastV[1] != null && !isNaN(lastV[1])) ? 'BUY'
                  : ((lastV[4] != null && !isNaN(lastV[4])) ? 'SELL' : null);
        r.long_stop = f(lastV[1]);
        r.short_stop = f(lastV[4]);
        // walk back to the most recent leg START - that is the flip bar
        var lo = Math.max(d.firstIndex(), end - 400);
        for (var j = end; j >= lo; j--) {
          var v = d.valueAt(j);
          if (!v) continue;
          var bs = v[2], ss = v[5];
          var isB = (bs != null && !isNaN(bs)), isS = (ss != null && !isNaN(ss));
          if (isB || isS) {
            r.flip_date = new Date(v[0] * 1000).toISOString().slice(0, 10);
            r.flip_type = isB ? 'BUY' : 'SELL';
            r.flip_level = f(isB ? bs : ss);
            r.bars_back = end - j;
            break;
          }
        }
      }
      if (mi.description === 'ZLSMA - Zero Lag LSMA') {
        var v1 = d.valueAt(end); r.zlsma = v1 ? f(v1[1]) : null;
      }
      // "Magical" = 20-period CCI on close, own OB/OS bands at +/-100
      if (mi.description && mi.description.indexOf('Magical') === 0) {
        var v2 = d.valueAt(end); r.magical = v2 ? f(v2[1]) : null;
      }
    }

    try {
      var b = cw.model().model().mainSeries().bars();
      var lv = b.valueAt(b.lastIndex());
      r.last = f(lv[4]);
      r.bar_date = new Date(lv[0] * 1000).toISOString().slice(0, 10);
      r.bar_count = b.size();

      // ------------------------------------------------------------------
      // REAL PRICES (added 2026-07-25) - r.last above is the HEIKIN-ASHI close,
      // not a price anyone can trade at. HA close is (O+H+L+C)/4, so it is a
      // smoothed average and cannot be inverted back to the real close.
      //
      // Measured across 487 US names on 2026-07-24: the HA close differs from
      // the real close by a median 0.59%, with 31% of names off by >1%, 12% by
      // >2% and a worst case of 5.3%. NVTS printed 11.49 against a real close of
      // 10.92; ARM printed 272.55 against 260.01. Every quoted entry, stop distance, risk-per-share and 2:1 target
      // built on that number inherited the error.
      //
      // Omar's 2026-07-25 call: SIGNALS stay on Heikin Ashi, PLANS use real
      // closes. So r.last stays HA (every indicator and gate is computed on it,
      // unchanged and still internally consistent) and the real prices are
      // captured ALONGSIDE it from the quote object, which is the untransformed
      // feed. Verified on XOM: bars() gave 157.08, quote gave 156.94, which is
      // the true 7/24 close.
      try {
        var q = cw.model().model().mainSeries().quotes();
        if (q) {
          r.real_last = f(q.last_price);        // live last trade
          r.real_close = f(q.regular_close);    // regular-session close (use for EOD plans)
          r.real_open = f(q.open_price);
          r.real_high = f(q.high_price);
          r.real_low = f(q.low_price);
          r.prev_close = f(q.prev_close_price);
          // second, independent currency source for the wrong-listing guard
          r.qccy = q.currency_code || null;
        }
        // The quote object streams in AFTER the symbol switch, so on a fast
        // sweep it can still be empty when we read it (SJM did exactly this on
        // the 2026-07-25 test: currency present, prices null). A missing real
        // price is not cosmetic - it silently sends the plan back to the HA
        // number - so flag it explicitly rather than leaving a null to be
        // shrugged at downstream.
        if (r.real_close == null && r.real_last == null) {
          r.real_price_missing = true;
        }
      } catch (e) { r.quoteErr = String(e); r.real_price_missing = true; }

      // ------------------------------------------------------------------
      // REGIME + LIQUIDITY - captured on every sweep since 2026-07-22.
      // The Chandelier stack is blind to long-term trend; the regime filter
      // (HQ Swing v1's actual edge) is a MANDATORY gate, so it is measured
      // here rather than in a second pass that can be forgotten.
      // ------------------------------------------------------------------
      var A = [];
      for (var i = b.firstIndex(); i <= b.lastIndex(); i++) {
        var v = b.valueAt(i);
        if (v) A.push({h: v[2], l: v[3], c: v[4], v: v[5]});
      }
      var n = A.length;

      // ATR(14) on COMPLETED bars only (excludes the forming bar, which would
      // understate range mid-session). Feeds the atr_floor gate: a stop closer
      // than 1x ATR sits inside normal daily noise and gets hit by nothing
      // happening. FRT on 2026-07-22 was the case that forced this - a 0.82x
      // ATR stop passed the automated stack and had to be caught by hand.
      if (n >= 17) {
        var end2 = n - 1, trs = [];
        for (var a = end2 - 14; a < end2; a++) {
          if (a < 1) continue;
          trs.push(Math.max(A[a].h - A[a].l,
                            Math.abs(A[a].h - A[a - 1].c),
                            Math.abs(A[a].l - A[a - 1].c)));
        }
        if (trs.length) {
          var sum2 = 0;
          for (var b2 = 0; b2 < trs.length; b2++) sum2 += trs[b2];
          r.atr = f(sum2 / trs.length);
          r.atr_pct = f(r.atr / A[n - 1].c * 100);
        }
      }

      // average dollar volume over the last 20 COMPLETED bars (excl. today)
      if (n >= 22) {
        var s = 0, k = 0;
        for (var j = n - 21; j < n - 1; j++) { if (A[j].v) { s += A[j].v; k++; } }
        if (k) {
          r.avg_vol_20d = Math.round(s / k);
          r.avg_dollar_vol = Math.round((s / k) * A[n - 1].c);
        }
      }

      if (n >= 210) {
        var sma = function (kk, off) {
          off = off || 0; var t = 0;
          for (var i2 = n - kk - off; i2 < n - off; i2++) t += A[i2].c;
          return t / kk;
        };
        var per = 14, tr = [], pdm = [], ndm = [];
        for (var i3 = 1; i3 < n; i3++) {
          var up = A[i3].h - A[i3 - 1].h, dn = A[i3 - 1].l - A[i3].l;
          pdm.push(up > dn && up > 0 ? up : 0);
          ndm.push(dn > up && dn > 0 ? dn : 0);
          tr.push(Math.max(A[i3].h - A[i3].l,
                           Math.abs(A[i3].h - A[i3 - 1].c),
                           Math.abs(A[i3].l - A[i3 - 1].c)));
        }
        var wil = function (arr) {
          var t = 0; for (var q = 0; q < per; q++) t += arr[q];
          var o = [t];
          for (var q2 = per; q2 < arr.length; q2++) { t = t - t / per + arr[q2]; o.push(t); }
          return o;
        };
        var TR = wil(tr), PD = wil(pdm), ND = wil(ndm), dxa = [];
        for (var i4 = 0; i4 < TR.length; i4++) {
          var pp = 100 * PD[i4] / TR[i4], qq = 100 * ND[i4] / TR[i4];
          dxa.push(100 * Math.abs(pp - qq) / (pp + qq));
        }
        var t2 = 0; for (var i5 = 0; i5 < per; i5++) t2 += dxa[i5];
        var adxa = [t2 / per];
        for (var i6 = per; i6 < dxa.length; i6++) {
          adxa.push((adxa[adxa.length - 1] * (per - 1) + dxa[i6]) / per);
        }
        var s200 = sma(200), s200p = sma(200, 20), s50 = sma(50), px = A[n - 1].c;
        r.sma200 = f(s200);
        r.sma50 = f(s50);
        r.sma200_rising = s200 > s200p;
        r.pct_vs_200 = f((px / s200 - 1) * 100);
        r.above_50 = px > s50;
        r.adx = f(adxa[adxa.length - 1]);
        r.plus_di = f(100 * PD[PD.length - 1] / TR[TR.length - 1]);
        r.minus_di = f(100 * ND[ND.length - 1] / TR[TR.length - 1]);
        r.regime = (r.pct_vs_200 < -10) ? 'DEEP-FAIL'
                 : (r.pct_vs_200 < 0) ? 'REPAIR'
                 : (r.sma200_rising && r.above_50) ? 'PASS' : 'REPAIR';
      } else {
        r.regime = null;   // not enough history - gate treats this as a FAIL
      }
    } catch (e) { r.regimeErr = String(e); }

    try {
      var msi = cw.model().model().mainSeries().symbolInfo();
      if (msi) {
        r.rname = msi.name; r.rfull = msi.full_name; r.rdesc = msi.description;
        r.rccy = msi.currency_code; r.rtype = msi.type;
      }
    } catch (e) {}

    r.style = chartStyle();
    r.style_name = STYLE_NAMES[r.style] || ('unknown:' + r.style);
    // fingerprint EXCLUDES identity on purpose - see staleness note above
    r.fp = String(r.zlsma) + '|' + String(r.magical) + '|' + String(r.last)
         + '|' + String(r.flip_date);
    return r;
  };

  window.__ogSweep = function (symbols, tag, allowOtherStyle) {
    var style = chartStyle();
    if (style !== 8 && !allowOtherStyle) {
      return 'REFUSED: chart is ' + (STYLE_NAMES[style] || style)
           + ', not Heikin Ashi. Standing decision 2026-07-23 is Heikin Ashi. '
           + 'Switch with chart_set_type HeikinAshi, or pass allowOtherStyle=true.';
    }

    var cw = widget();
    window.__og = {tag: tag, style: style, style_name: STYLE_NAMES[style],
                   done: false, idx: 0, total: symbols.length,
                   results: [], errs: []};
    var sleep = function (ms) { return new Promise(function (r) { setTimeout(r, ms); }); };
    var bare = function (s) { return String(s || '').toUpperCase().split(':').pop(); };

    (async function () {
      var prev = null;
      for (var k = 0; k < symbols.length; k++) {
        var sym = symbols[k];
        window.__og.idx = k;
        try {
          cw.setSymbol(sym);
          await sleep(700);
          var r = null, ok = false, why = 'timeout', lastfp = null, stable = 0;
          for (var t = 0; t < 80; t++) {
            await sleep(160);
            try { r = window.__ogRead(); } catch (e) { r = null; continue; }
            if (!r || !r.rname) { why = 'no-symbolinfo'; stable = 0; continue; }
            if (bare(r.rname) !== bare(sym)) { why = 'identity:' + r.rname; stable = 0; continue; }
            if (r.last == null || r.ce_mode == null || r.zlsma == null
                || r.magical == null || !(r.bar_count > 60)) {
              why = 'incomplete'; stable = 0; continue;
            }
            var fp = r.fp;
            if (prev !== null && fp === prev) { why = 'stale-values'; stable = 0; continue; }
            if (fp === lastfp) { stable++; } else { stable = 1; lastfp = fp; }
            if (stable >= 2) { ok = true; why = 'ok'; break; }
          }
          // The quote object streams in independently of the bars, so it can
          // still be empty when the indicators have already settled. Top it up
          // rather than fall back to the Heikin-Ashi number, which is not a
          // tradeable price. Deliberately does NOT fail the row: a missing quote
          // costs us a plan price, and failing would cost us the SIGNAL too.
          // Budget 5s: measured on SJM 2026-07-25, whose indicators settled fast
          // but whose quote had not streamed yet at 1.6s and HAD arrived when
          // checked later. Only names that actually need it pay this.
          if (ok && r && r.real_price_missing) {
            for (var qt = 0; qt < 25; qt++) {
              await sleep(200);
              try {
                var q2 = cw.model().model().mainSeries().quotes();
                if (q2 && (q2.regular_close != null || q2.last_price != null)) {
                  r.real_last = f(q2.last_price);
                  r.real_close = f(q2.regular_close);
                  r.real_open = f(q2.open_price);
                  r.real_high = f(q2.high_price);
                  r.real_low = f(q2.low_price);
                  r.prev_close = f(q2.prev_close_price);
                  r.qccy = q2.currency_code || r.qccy;
                  delete r.real_price_missing;
                  break;
                }
              } catch (e) { r.quoteRetryErr = String(e); }   // never swallow silently again
            }
          }
          if (!r) r = {};
          r.req = sym; r.ok = ok; r.why = why;
          if (ok) prev = lastfp;
          window.__og.results.push(r);
        } catch (e) {
          window.__og.errs.push({sym: sym, e: String(e)});
        }
      }
      window.__og.done = true;
    })();

    return 'started ' + symbols.length + ' [' + tag + '] on ' + STYLE_NAMES[style];
  };

  return 'og-sweep-runner installed (chart: ' + STYLE_NAMES[chartStyle()] + ')';
})()
