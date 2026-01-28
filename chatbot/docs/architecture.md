# アーキテクチャ設計書

## アーキテクチャ概要

本システムは、シンプルなクライアント・サーバーアーキテクチャを採用する。
開発の容易さとデモのしやすさを重視し、モノリシックな構成とする。

## 技術選定

### 推奨構成（Streamlit版）

最もシンプルで素早く開発可能な構成。

```
┌────────────────────────────────────────────┐
│              Streamlit App                  │
│  ┌──────────────────────────────────────┐  │
│  │          Frontend (Auto-generated)    │  │
│  ├──────────────────────────────────────┤  │
│  │          Backend (Python)             │  │
│  │  ・Chat Logic                         │  │
│  │  ・Gemini API Integration             │  │
│  │  ・RAG (LangChain)                    │  │
│  └──────────────────────────────────────┘  │
└────────────────────────────────────────────┘
```

**技術スタック**:
| レイヤー | 技術 |
|----------|------|
| フレームワーク | Streamlit |
| LLM連携 | LangChain + google-generativeai |
| RAG | LangChain + ChromaDB |
| 言語 | Python 3.11+ |

**メリット**:
- 最小限のコードで動作するUIが構築可能
- Pythonのみで完結
- RAG実装が容易（LangChain活用）

### 代替構成（Next.js版）

よりカスタマイズ性の高いUI が必要な場合。

```
┌──────────────────────┐    ┌──────────────────────┐
│   Frontend (Next.js)  │───│   Backend (API)      │
│  ・React Components   │    │  ・Next.js API Routes│
│  ・Tailwind CSS       │    │  ・Gemini SDK        │
└──────────────────────┘    └──────────────────────┘
```

**技術スタック**:
| レイヤー | 技術 |
|----------|------|
| フレームワーク | Next.js 14 (App Router) |
| UI | React + Tailwind CSS |
| LLM連携 | @google/generative-ai |
| デプロイ | Vercel |

### 代替構成（Dify版）

ノーコード/ローコードで開発する場合。

```
┌────────────────────────────────────────────┐
│                 Dify Platform              │
│  ┌──────────────────────────────────────┐  │
│  │          Visual Workflow Builder      │  │
│  │  ・Prompt Template                    │  │
│  │  ・Knowledge Base (RAG)               │  │
│  │  ・Model Configuration                │  │
│  └──────────────────────────────────────┘  │
└────────────────────────────────────────────┘
```

**メリット**:
- コーディング不要
- 学生向け無料枠拡大可能
- 組み込みRAG機能

## ディレクトリ構成

### Streamlit版

```
chatbot/
├── docs/                    # 設計ドキュメント
│   ├── requirements.md
│   ├── design.md
│   └── architecture.md
├── src/                     # ソースコード
│   ├── app.py              # メインアプリケーション
│   ├── chat_service.py     # チャットロジック
│   ├── llm_client.py       # Gemini API クライアント
│   └── rag/                # RAG モジュール
│       ├── __init__.py
│       ├── document_loader.py
│       ├── embeddings.py
│       └── retriever.py
├── data/                    # 知識ベースデータ
│   └── documents/
├── tests/                   # テストコード
│   ├── test_chat_service.py
│   └── test_llm_client.py
├── .env.example            # 環境変数テンプレート
├── requirements.txt        # Python依存関係
└── README.md               # プロジェクト説明
```

### Next.js版

```
chatbot/
├── docs/                    # 設計ドキュメント
├── src/
│   ├── app/                # Next.js App Router
│   │   ├── page.tsx       # メインページ
│   │   ├── layout.tsx     # レイアウト
│   │   └── api/
│   │       └── chat/
│   │           └── route.ts  # Chat API
│   ├── components/         # Reactコンポーネント
│   │   ├── ChatInput.tsx
│   │   ├── ChatMessage.tsx
│   │   └── ChatWindow.tsx
│   └── lib/                # ユーティリティ
│       └── gemini.ts      # Gemini クライアント
├── .env.local             # 環境変数
├── package.json
├── tsconfig.json
└── README.md
```

## 環境構成

### 開発環境

```
┌─────────────────────────────────────────┐
│           Local Development              │
│  ・ローカルサーバー (localhost:8501)    │
│  ・ホットリロード有効                    │
│  ・.env ファイルで環境変数管理          │
└─────────────────────────────────────────┘
```

### 本番環境（オプション）

```
┌─────────────────────────────────────────┐
│          Vercel / Streamlit Cloud       │
│  ・自動デプロイ (GitHub連携)            │
│  ・環境変数は管理画面から設定           │
│  ・HTTPS自動対応                        │
└─────────────────────────────────────────┘
```

## 開発フロー

### Phase 1: MVP（最低限の動作）

```
Week 1:
├── 環境構築
├── 基本チャットUI実装
└── Gemini API連携
```

**成果物**: テキスト入力に対してGemini APIが応答するシンプルなチャットボット

### Phase 2: 機能拡張（RAG実装）

```
Week 2:
├── ドキュメントローダー実装
├── Embedding設定
├── Vector Store構築
└── Retriever統合
```

**成果物**: 講座資料を参照して回答できるRAG機能付きチャットボット

### Phase 3: 品質向上・デモ準備

```
Week 3:
├── UI/UXの改善
├── エラーハンドリング強化
├── テスト実施
└── 動画撮影
```

**成果物**: 提出用動画（約1分間）

## 依存関係

### Python (Streamlit版)

```txt
streamlit>=1.28.0
langchain>=0.1.0
langchain-google-genai>=0.0.6
chromadb>=0.4.0
python-dotenv>=1.0.0
```

### Node.js (Next.js版)

```json
{
  "dependencies": {
    "next": "^14.0.0",
    "react": "^18.2.0",
    "@google/generative-ai": "^0.1.0"
  },
  "devDependencies": {
    "typescript": "^5.0.0",
    "tailwindcss": "^3.3.0"
  }
}
```

## 判断基準とトレードオフ

| 観点 | Streamlit | Next.js | Dify |
|------|-----------|---------|------|
| 開発速度 | 高 | 中 | 最高 |
| カスタマイズ性 | 中 | 高 | 低 |
| RAG実装容易性 | 高 | 中 | 最高 |
| 学習コスト | 低 | 中 | 最低 |
| デプロイ容易性 | 高 | 高 | 高 |

**推奨**: 時間制約を考慮し、**Streamlit版**での開発を推奨する。
RAG実装が必要な場合はLangChainとの親和性が高く、迅速に開発可能。
