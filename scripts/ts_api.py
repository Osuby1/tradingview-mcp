"""TradeStation Web API helper (v3, Auth0 flow).

Credentials live in ~/.tradestation/credentials.json (NEVER in the repo):
  { client_id, client_secret, refresh_token?, access_token?, access_expires? }

One-time setup: python scripts/ts_auth.py  (browser login -> refresh token)
After that any script can call ts_quotes([...]) headlessly.

Note from the key-approval letter: professional market-data subscribers may
get EXPIRING refresh tokens (24h absolute -> daily re-auth). Non-pro keys
get non-expiring refresh tokens. If quotes start failing with auth errors,
rerun ts_auth.py.
"""
import json
import time
from pathlib import Path

import requests

CREDS_PATH = Path.home() / ".tradestation" / "credentials.json"
TOKEN_URL = "https://signin.tradestation.com/oauth/token"
API = "https://api.tradestation.com/v3"


def _load():
    return json.loads(CREDS_PATH.read_text())


def _save(creds):
    CREDS_PATH.write_text(json.dumps(creds, indent=1))


def get_access_token():
    """Return a valid access token, refreshing via the stored refresh token."""
    creds = _load()
    if creds.get("access_token") and time.time() < creds.get("access_expires", 0) - 60:
        return creds["access_token"]
    if not creds.get("refresh_token"):
        raise RuntimeError("No refresh token - run: python scripts/ts_auth.py")
    r = requests.post(TOKEN_URL, data={
        "grant_type": "refresh_token",
        "client_id": creds["client_id"],
        "client_secret": creds["client_secret"],
        "refresh_token": creds["refresh_token"],
    }, timeout=30)
    r.raise_for_status()
    tok = r.json()
    creds["access_token"] = tok["access_token"]
    creds["access_expires"] = time.time() + int(tok.get("expires_in", 1200))
    if tok.get("refresh_token"):  # rotation, if enabled on the key
        creds["refresh_token"] = tok["refresh_token"]
    _save(creds)
    return creds["access_token"]


def ts_quotes(symbols):
    """Snapshot quotes for a list of symbols (e.g. ['CLU26','RBU26']).
    Returns {symbol: {Last, Close, PreviousClose, ...}} for symbols that priced.
    """
    token = get_access_token()
    r = requests.get(f"{API}/marketdata/quotes/{','.join(symbols)}",
                     headers={"Authorization": f"Bearer {token}"}, timeout=30)
    r.raise_for_status()
    out = {}
    for q in r.json().get("Quotes", []):
        if q.get("Error") or not q.get("Last") or q.get("Last") == "0":
            continue
        out[q["Symbol"]] = q
    return out


def available():
    """True if headless auth is ready (refresh token stored)."""
    try:
        return bool(_load().get("refresh_token"))
    except Exception:
        return False
