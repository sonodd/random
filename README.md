# Random Code Repository

機能確認やテスト開発のための実験的なコードを集めたリポジトリです。

## ディレクトリ構造

```
random/
├── python/       # ローカルPython実行用
├── colab/        # Google Colab実行用
└── planning/     # 設計書・アイデア
```

## python/ - ローカルPython実行用

| プロジェクト | 説明 | 状態 |
|-------------|------|------|
| [url-summarizer](./python/url-summarizer/) | URLからページ内容をMarkdownに要約 | ✅ 動作可 |
| [word-counter](./python/word-counter/) | Webページの単語出現頻度をカウント | ✅ 動作可 |

## colab/ - Google Colab実行用

| プロジェクト | 説明 | 状態 |
|-------------|------|------|
| [openai-langchain](./colab/openai-langchain/) | OpenAI API + LangChainでテキスト分類 | ✅ 動作可 |

## planning/ - 設計書・アイデア

| プロジェクト | 説明 | 状態 |
|-------------|------|------|
| [chatbot](./planning/chatbot/) | AIチャットボットの設計書（講座課題） | 📝 設計のみ |
| [ideas/zundoko](./planning/ideas/zundoko/) | ズンドコキヨシ実験のアイデア | 💡 未実装 |
| [ideas/stats-r-comparison](./planning/ideas/stats-r-comparison/) | R言語比較の統計分析アイデア | 💡 未実装 |

## 使用技術

- **言語**: Python
- **AI/ML**: OpenAI API, LangChain
- **Web**: requests, BeautifulSoup, Selenium
- **環境**: ローカルPython, Google Colab

## ライセンス

[MIT License](./LICENSE)
