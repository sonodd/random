#これはなんのファイルだ？

# #pythonのファイルとして実行する
# #ハローワールドを書く
# print("Hello World")

import requests
from bs4 import BeautifulSoup
import re
from collections import Counter

# WebサイトのURLを指定
url = "https://www.wantanblog.com/entry/2021/12/25/223145"

# URLからHTMLを取得
response = requests.get(url)
content = response.content

# BeautifulSoupでHTMLを解析
soup = BeautifulSoup(content, "html.parser")

# HTML内のテキストを取得
text = soup.get_text()

# 単語に分割し、小文字に変換
words = re.findall(r'\w+', text.lower())

# 単語の出現回数をカウント
word_count = Counter(words)

# 最も頻繁に出現する単語を表示
most_common_word, frequency = word_count.most_common(1)[0]
print(f"最も頻繁に出現する単語: {most_common_word}, 出現回数: {frequency}")

