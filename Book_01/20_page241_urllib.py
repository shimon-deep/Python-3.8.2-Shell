## 独学プログラマー 
## 20章 知識を1つにまとめる P.238～245
# Thanks so much for reading my book. Feel free to contact me at cory[at]theselftaughtprogrammer.io.

# ▼▼ チャレンジ 1 ▼▼
import urllib.request
from bs4 import BeautifulSoup
import os
from datetime import datetime
import csv

class Scraper:
    def __init__(self, site, filename):
        self.site = site
        self.wd = os.getcwd() # 本実行fileのディレクトリを取得
        self.filename = self.wd + "/" + filename + ".csv"
        
    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "https://www" in url:
                print("\n" + url)
                self.write_file(url)

    def write_file(self, writeMsg):
        with open(self.filename, 'a', newline ="") as f: # 'a'：追記
            self.w = csv.writer(f)
            self.w.writerow([writeMsg])                  # []で囲むことで、1オブジェクトとしてみなす

# エントリポイント
news = "https://news.google.com/"  # GoogleニュースのURL
date = datetime.now()              # 現在時刻を取得
strDate = str(date.year) + str(date.month) + str(date.day) + \
          str(date.hour) + str(date.minute)
Scraper(news, strDate).scrape()

# ▲▲ チャレンジ 1 ▲▲

"""
出力ファイル名：2020542246.csv

    ▼▼ 出力結果 ▼▼
https://www.google.com/intl/en/about/products
https://www.google.com/webhp
https://www.youtube.com/?gl=US
https://www.google.com/calendar
https://www.google.com/chrome/?brand=CHZO&utm_source=google.com&utm_medium=desktop-app-launcher&utm_campaign=desktop-app-launcher&utm_content=chrome-logo&utm_keyword=CHZO
https://www.google.com/shopping?hl=en&source=og
https://www.google.com/finance
https://www.blogger.com/
https://www.google.com/save
https://www.google.com/intl/en/about/products
https://www.google.com/producer/app/privacy?hl=en-US
https://www.google.com/producer/app/tos?hl=en-US
https://www.google.com/about
    ▲▲ 出力結果 ▲▲ """

# 解答URL：http://tinyurl.com/gkv6fuh
