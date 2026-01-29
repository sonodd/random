# Random Code Repository

機能確認やテスト開発のための実験的なコードを集めたリポジトリです。

## カテゴリ一覧

| カテゴリ | 説明 | プロジェクト数 |
|---------|------|---------------|
| [ai-ml/](./ai-ml/) | AI・機械学習関連 | 1 |
| [data-analysis/](./data-analysis/) | データ分析 | 1 |
| [algorithms/](./algorithms/) | アルゴリズム・ロジック | 1 |
| [web/](./web/) | Web関連（スクレイピング等） | 1 |

## プロジェクト一覧

| プロジェクト | 説明 | 状態 |
|-------------|------|------|
| [ai-ml/openai-langchain](./ai-ml/openai-langchain/) | OpenAI APIとLangChainでテキスト分類 | ✅ 動作確認済 |
| [data-analysis/stats-r-comparison](./data-analysis/stats-r-comparison/) | NBAデータを使った統計分析（R比較） | ✅ 動作確認済 |
| [algorithms/zundoko](./algorithms/zundoko/) | ズンドコキヨシ実験 | ✅ 動作確認済 |
| [web/scraping](./web/scraping/) | BeautifulSoupでWebスクレイピング | ✅ 動作確認済 |

## ディレクトリ構造

```
random/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── .gitignore
│
├── ai-ml/                      # AI・機械学習
│   └── openai-langchain/
│
├── data-analysis/              # データ分析
│   └── stats-r-comparison/
│
├── algorithms/                 # アルゴリズム
│   └── zundoko/
│
└── web/                        # Web関連
    └── scraping/
```

## 使用技術

- **言語**: Python
- **AI/ML**: OpenAI API, LangChain
- **データ処理**: pandas, collections
- **Web**: requests, BeautifulSoup
- **環境**: Jupyter Notebook, Google Colab

## クイックスタート

```bash
# リポジトリをクローン
git clone https://github.com/sonodd/random.git
cd random

# 各プロジェクトのREADMEを参照して環境構築
```

## コントリビューション

新しいコードを追加する際は [CONTRIBUTING.md](./CONTRIBUTING.md) を参照してください。

## ライセンス

このプロジェクトは [MIT License](./LICENSE) の下で公開されています。
