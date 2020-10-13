import requests

url = "http://developer-ankiwoong.tistory.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Whale/2.8.107.16 Safari/537.36"
}

res = requests.get(url, headers=headers)
res.raise_for_status()

with open("result.html", "w", encoding="utf-8") as f:
    f.write(res.text)