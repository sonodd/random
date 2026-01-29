# Random Code Repository

機能確認やテスト開発のための実験的なコードを集めたリポジトリです。

## ディレクトリ構造

```
random/
├── scripts/      # 実行可能なPythonスクリプト
├── notebooks/    # Jupyter/Google Colab用ノートブック
└── docs/         # 設計書・ドキュメント・アイデア
```

## scripts/ - Pythonスクリプト

ローカル環境で実行可能なスクリプト群。

| プロジェクト | 説明 | 状態 |
|-------------|------|------|
| [url-summarizer](./scripts/url-summarizer/) | URLからページ内容をMarkdownに要約 | ✅ 動作可 |
| [sonosei-crawler](./scripts/sonosei-crawler/) | listen.styleからテキストをダウンロード | ✅ 動作可 |
| [word-counter](./scripts/word-counter/) | Webページの単語出現頻度をカウント | ✅ 動作可 |

## notebooks/ - Jupyter/Colab用

Google Colabなどで実行するノートブック。

| プロジェクト | 説明 | 状態 |
|-------------|------|------|
| [openai-langchain](./notebooks/openai-langchain/) | OpenAI API + LangChainでテキスト分類 | ✅ 動作可 |

## docs/ - ドキュメント

設計書やアイデアメモ。

| プロジェクト | 説明 | 状態 |
|-------------|------|------|
| [chatbot](./docs/chatbot/) | AIチャットボットの設計書（講座課題） | 📝 設計のみ |
| [ideas/zundoko](./docs/ideas/zundoko/) | ズンドコキヨシ実験のアイデア | 💡 未実装 |
| [ideas/stats-r-comparison](./docs/ideas/stats-r-comparison/) | R言語比較の統計分析アイデア | 💡 未実装 |

## 使用技術

- **言語**: Python
- **AI/ML**: OpenAI API, LangChain
- **Web**: requests, BeautifulSoup, Selenium
- **環境**: ローカルPython, Google Colab

## ライセンス

[MIT License](./LICENSE)
