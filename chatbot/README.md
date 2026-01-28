# AI チャットボット

講座最終課題として開発するAIチャットボットプロジェクト。

## 概要

Gemini APIを活用したWebベースのAIチャットボット。
RAG（Retrieval-Augmented Generation）機能により、講座資料を参照した回答が可能。

## プロジェクト構成

```
chatbot/
├── docs/                    # 設計ドキュメント
│   ├── requirements.md     # 要件定義書
│   ├── design.md           # システム設計書
│   └── architecture.md     # アーキテクチャ設計書
├── src/                     # ソースコード（実装時に作成）
├── data/                    # 知識ベースデータ（実装時に作成）
└── README.md               # このファイル
```

## 技術スタック

| カテゴリ | 技術 |
|----------|------|
| LLM API | Google Gemini API |
| フレームワーク | Streamlit（推奨） |
| RAG | LangChain + ChromaDB |
| 言語 | Python 3.11+ |

## クイックスタート

### 前提条件

- Python 3.11以上
- Gemini API キー

### セットアップ

```bash
# リポジトリをクローン
git clone <repository-url>
cd chatbot

# 仮想環境を作成
python -m venv venv
source venv/bin/activate  # Linux/Mac
# または
.\venv\Scripts\activate   # Windows

# 依存関係をインストール
pip install -r requirements.txt

# 環境変数を設定
cp .env.example .env
# .envファイルを編集してGEMINI_API_KEYを設定
```

### 実行

```bash
streamlit run src/app.py
```

ブラウザで `http://localhost:8501` を開く。

## 開発スケジュール

| フェーズ | 内容 | 期間 |
|---------|------|------|
| Phase 1 | MVP（基本チャット機能） | Week 1 |
| Phase 2 | RAG機能実装 | Week 2 |
| Phase 3 | 品質向上・動画作成 | Week 3 |

## 提出要件

- **期限**: 2026年2月15日 23:59
- **成果物**: 動作動画（約1分間）
- **内容**: 講座関連の質問を含むデモ

## ドキュメント

詳細は `docs/` ディレクトリを参照：

- [要件定義書](docs/requirements.md) - 機能要件・非機能要件
- [システム設計書](docs/design.md) - モジュール設計・データフロー
- [アーキテクチャ設計書](docs/architecture.md) - 技術選定・ディレクトリ構成

## ライセンス

Private - 講座課題用
