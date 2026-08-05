"""One-time TradeStation Web API login (Auth0 authorization-code flow).

Run:  python scripts/ts_auth.py  [--port 3000]
A browser window opens -> log in to TradeStation -> the local callback
captures the code -> a refresh token is saved to ~/.tradestation/credentials.json.
Tokens are never printed.

If TradeStation rejects the redirect URI, the key was registered with a
different one - tell Claude the registered URI and rerun with matching --port.
"""
import argparse
import http.server
import json
import threading
import urllib.parse
import webbrowser
from pathlib import Path

import requests

CREDS_PATH = Path.home() / ".tradestation" / "credentials.json"
AUTH_URL = "https://signin.tradestation.com/authorize"
TOKEN_URL = "https://signin.tradestation.com/oauth/token"
SCOPE = "openid offline_access profile MarketData ReadAccount"

code_holder = {}


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        qs = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        if "code" in qs:
            code_holder["code"] = qs["code"][0]
            body = b"<h2>TradeStation login captured - you can close this tab.</h2>"
        else:
            body = b"<h2>No code in callback - check the browser URL for an error message.</h2>"
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *a):  # silence request logging
        pass


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=3000)
    args = ap.parse_args()
    redirect = f"http://localhost:{args.port}"

    creds = json.loads(CREDS_PATH.read_text())
    params = {
        "response_type": "code",
        "client_id": creds["client_id"],
        "redirect_uri": redirect,
        "audience": "https://api.tradestation.com",
        "scope": SCOPE,
    }
    url = AUTH_URL + "?" + urllib.parse.urlencode(params)

    server = http.server.HTTPServer(("localhost", args.port), Handler)
    threading.Thread(target=server.handle_request, daemon=True).start()
    print(f"Opening browser for TradeStation login (callback on {redirect})...")
    webbrowser.open(url)
    print("Waiting for login (up to 5 minutes)...")
    server.timeout = 300
    import time
    for _ in range(300):
        if code_holder.get("code"):
            break
        time.sleep(1)
    if not code_holder.get("code"):
        raise SystemExit("Timed out waiting for the login callback.")

    r = requests.post(TOKEN_URL, data={
        "grant_type": "authorization_code",
        "client_id": creds["client_id"],
        "client_secret": creds["client_secret"],
        "code": code_holder["code"],
        "redirect_uri": redirect,
    }, timeout=30)
    r.raise_for_status()
    tok = r.json()
    if "refresh_token" not in tok:
        raise SystemExit("No refresh token returned - was 'offline_access' scope granted?")
    creds["refresh_token"] = tok["refresh_token"]
    CREDS_PATH.write_text(json.dumps(creds, indent=1))
    print("SUCCESS: refresh token saved to", CREDS_PATH)
    print("Headless TradeStation data is now available to the feed scripts.")


if __name__ == "__main__":
    main()
