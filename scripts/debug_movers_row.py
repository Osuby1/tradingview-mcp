import re
import requests

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
    )
}
r = requests.get("https://stockanalysis.com/markets/gainers/", headers=HEADERS, timeout=30)
html = r.text
head = re.search(r"<thead[^>]*>(.*?)</thead>", html, re.S)
if head:
    ths = [re.sub(r"<[^>]+>", "", th).strip() for th in re.findall(r"<th[^>]*>(.*?)</th>", head.group(1), re.S)]
    print("HEADERS:", ths)
body = re.search(r"<tbody[^>]*>(.*?)</tbody>", html, re.S)
tr = re.search(r"<tr[^>]*>(.*?)</tr>", body.group(1), re.S)
cells = [re.sub(r"<[^>]+>", "", c).strip() for c in re.findall(r"<td[^>]*>(.*?)</td>", tr.group(1), re.S)]
print("ROW:", cells)
