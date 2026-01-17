# OpenAI API + LangChain テキスト分類

OpenAI APIとLangChainフレームワークを使用したテキスト分類の実験です。

## 概要

単語リストを「室内」「屋外」「その他」のカテゴリに分類し、結果を集計します。
「その他」の割合が高い場合は動的に新しいカテゴリを生成します。

## 機能

- GPT-4oモデルによるテキスト分類
- LangChainを使った分類パイプライン
- 動的カテゴリ生成（反復的改善）
- pandasによる結果集計

## 必要な環境

- Python 3.8+
- Google Colab（推奨）

## 依存ライブラリ

```
openai
langchain
langchain-openai
langchain-experimental
pandas
```

## 使い方

1. Google Colabでノートブックを開く
2. Colabのシークレット機能でOpenAI APIキーを設定
3. セルを順番に実行

## APIキーの設定

Google Colabの場合：
```python
from google.colab import userdata
api_key = userdata.get('OPENAI_API_KEY')
```

## ファイル構成

```
openai-langchain/
├── README.md
└── using_openai_api_and_langchain.ipynb
```
