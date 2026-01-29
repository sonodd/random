# URL Summarizer

## 概要

このプログラムは、指定されたURLのウェブページの内容を取得し、そのページの概要と主要なリンクをまとめたMarkdownファイルを生成します。出力される内容は、A4用紙1枚程度の文字数（約1600文字）に調整されます。

## 機能

- 指定されたURLからHTMLコンテンツを取得します。
- ページのタイトル、主要なコンテンツ、リンクを抽出します。
- コンテンツをMarkdown形式に変換します。
- 結果を `url_summarizer_summary.md` というファイル名で保存します。

## 必要なもの

- Python 3.6以上

## インストール方法

以下のコマンドを実行して、必要なライブラリをインストールします。

```bash
pip install -r url_summarizer_requirements.txt
```

## 使い方

以下のコマンドを実行します。`<URL>`の部分に、要約したいウェブページのURLを指定してください。

```bash
python url_summarizer_main.py <URL>
```

### 例

```bash
python url_summarizer_main.py https://www.python.org/
```

処理が完了すると、同じディレクトリに`url_summarizer_summary.md`ファイルが生成されます。
