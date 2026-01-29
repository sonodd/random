# Webスクレイピング

BeautifulSoupを使用したWebスクレイピングのサンプルコードです。

## 概要

指定したURLからHTMLを取得し、テキストを抽出して単語の出現頻度をカウントします。

## 機能

- requestsによるHTMLの取得
- BeautifulSoupによるHTML解析
- 正規表現によるテキスト抽出
- Counterによる単語頻度集計

## 必要な環境

- Python 3.8+

## 依存ライブラリ

```
requests
beautifulsoup4
```

## インストール

```bash
pip install requests beautifulsoup4
```

## 使い方

```bash
python test2.py
```

## 注意事項

- スクレイピング対象サイトの利用規約を確認してください
- 過度なリクエストは避けてください
- robots.txt を尊重してください

## ファイル構成

```
scraping/
├── README.md
└── test2.py
```
