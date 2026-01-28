# アーキテクチャ設計書

## アーキテクチャ概要

本システムは、Next.js + Vercelを採用したモダンなWebアプリケーション構成とする。
Vercelへのデプロイにチャレンジし、本番環境での動作を目指す。

## 技術選定

### 推奨構成（Next.js + Vercel）

Vercelの無料枠（Hobbyプラン）を活用し、本番デプロイまで行う構成。

```
┌─────────────────────────────────────────────────────────────┐
│                     Vercel Platform                          │
│  ┌───────────────────────────────────────────────────────┐  │
│  │                   Next.js Application                  │  │
│  │  ┌─────────────────┐    ┌─────────────────────────┐   │  │
│  │  │  Frontend       │    │  API Routes              │   │  │
│  │  │  ・React        │    │  ・/api/chat            │   │  │
│  │  │  ・Tailwind CSS │    │  ・Gemini API連携       │   │  │
│  │  │  ・Chat UI      │    │  ・RAG処理（オプション）│   │  │
│  │  └─────────────────┘    └─────────────────────────┘   │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    External Services                         │
│  ┌──────────────────────────────────────────────────┐      │
│  │              Google Gemini API                     │      │
│  └──────────────────────────────────────────────────┘      │
└─────────────────────────────────────────────────────────────┘
```

**技術スタック**:

| レイヤー | 技術 | バージョン |
|----------|------|-----------|
| フレームワーク | Next.js (App Router) | 14.x |
| 言語 | TypeScript | 5.x |
| UI | React + Tailwind CSS | React 18.x |
| LLM連携 | @google/generative-ai | 最新 |
| デプロイ | Vercel (Hobby Plan) | - |

**メリット**:
- Vercelへのワンクリックデプロイ
- 本番URLが即座に発行される
- GitHub連携で自動デプロイ
- Edge Functionsで高速レスポンス
- 無料枠で十分な機能

### 代替構成（Streamlit版）

シンプルさを優先する場合の選択肢。

```
┌────────────────────────────────────────────┐
│              Streamlit App                  │
│  ・Frontend (Auto-generated)               │
│  ・Backend (Python)                        │
│  ・Streamlit Cloud でデプロイ可能          │
└────────────────────────────────────────────┘
```

### 代替構成（Dify版）

ノーコード/ローコードで開発する場合。

```
┌────────────────────────────────────────────┐
│                 Dify Platform              │
│  ・Visual Workflow Builder                 │
│  ・組み込みRAG機能                         │
│  ・学生向け無料枠拡大可能                  │
└────────────────────────────────────────────┘
```

## ディレクトリ構成

### Next.js + Vercel版（推奨）

```
chatbot/
├── docs/                       # 設計ドキュメント
│   ├── requirements.md
│   ├── design.md
│   ├── architecture.md
│   └── testing.md
├── src/
│   ├── app/                    # Next.js App Router
│   │   ├── page.tsx           # メインページ（チャットUI）
│   │   ├── layout.tsx         # ルートレイアウト
│   │   ├── globals.css        # グローバルスタイル
│   │   └── api/
│   │       └── chat/
│   │           └── route.ts   # Chat API エンドポイント
│   ├── components/             # Reactコンポーネント
│   │   ├── ChatWindow.tsx     # チャットウィンドウ
│   │   ├── ChatMessage.tsx    # メッセージ表示
│   │   ├── ChatInput.tsx      # 入力フォーム
│   │   └── LoadingSpinner.tsx # ローディング表示
│   ├── lib/                    # ユーティリティ
│   │   ├── gemini.ts          # Gemini APIクライアント
│   │   └── types.ts           # 型定義
│   └── data/                   # 知識ベース（RAG用）
│       └── documents/
├── public/                     # 静的ファイル
├── tests/                      # テストコード
│   ├── components/
│   └── api/
├── .env.local                  # 環境変数（ローカル）
├── .env.example                # 環境変数テンプレート
├── .gitignore
├── next.config.js              # Next.js設定
├── tailwind.config.js          # Tailwind設定
├── tsconfig.json               # TypeScript設定
├── package.json
└── README.md
```

## 環境構成

### 開発環境

```
┌─────────────────────────────────────────┐
│           Local Development              │
│  ・localhost:3000                        │
│  ・ホットリロード有効                    │
│  ・.env.local で環境変数管理            │
└─────────────────────────────────────────┘

セットアップ:
$ npm install
$ cp .env.example .env.local
$ npm run dev
```

### 本番環境（Vercel）

```
┌─────────────────────────────────────────┐
│              Vercel Platform             │
│  ・自動デプロイ (GitHub Push時)         │
│  ・プレビューURL (PR作成時)             │
│  ・本番URL: https://xxx.vercel.app      │
│  ・環境変数はVercel管理画面で設定       │
│  ・HTTPS自動対応                        │
│  ・CDN配信                              │
└─────────────────────────────────────────┘

デプロイ手順:
1. GitHubリポジトリをVercelに接続
2. 環境変数(GEMINI_API_KEY)を設定
3. デプロイ実行（自動）
```

## Vercel デプロイ設定

### vercel.json（オプション）

```json
{
  "buildCommand": "npm run build",
  "outputDirectory": ".next",
  "framework": "nextjs",
  "regions": ["hnd1"]
}
```

### 環境変数

| 変数名 | 説明 | 設定場所 |
|--------|------|---------|
| `GEMINI_API_KEY` | Gemini API キー | Vercel管理画面 |
| `NEXT_PUBLIC_APP_URL` | アプリURL（オプション） | Vercel管理画面 |

## 開発フロー

### Phase 1: MVP（最低限の動作）

```
Week 1:
├── Next.js プロジェクト初期化
├── Tailwind CSS セットアップ
├── 基本チャットUI実装
├── Gemini API連携
└── Vercel初回デプロイ
```

**成果物**: Vercel上で動作するシンプルなチャットボット

### Phase 2: 機能拡張

```
Week 2:
├── UI/UXの改善（レスポンシブ対応）
├── ストリーミング応答の実装
├── 会話履歴の保持
└── RAG機能（オプション）
```

**成果物**: 講座資料を参照できるチャットボット

### Phase 3: 品質向上・デモ準備

```
Week 3:
├── エラーハンドリング強化
├── ローディング状態の改善
├── テスト実施
└── 動画撮影
```

**成果物**: 提出用動画（約1分間）

## 依存関係

### package.json

```json
{
  "name": "chatbot",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint",
    "test": "jest"
  },
  "dependencies": {
    "next": "^14.0.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "@google/generative-ai": "^0.21.0",
    "ai": "^3.0.0"
  },
  "devDependencies": {
    "typescript": "^5.0.0",
    "@types/node": "^20.0.0",
    "@types/react": "^18.2.0",
    "@types/react-dom": "^18.2.0",
    "tailwindcss": "^3.4.0",
    "postcss": "^8.4.0",
    "autoprefixer": "^10.4.0",
    "eslint": "^8.0.0",
    "eslint-config-next": "^14.0.0",
    "jest": "^29.0.0",
    "@testing-library/react": "^14.0.0"
  }
}
```

## 判断基準とトレードオフ

| 観点 | Next.js + Vercel | Streamlit | Dify |
|------|-----------------|-----------|------|
| 開発速度 | 中 | 高 | 最高 |
| カスタマイズ性 | **高** | 中 | 低 |
| 本番デプロイ | **最高** | 中 | 高 |
| UIの自由度 | **高** | 低 | 低 |
| 学習価値 | **高** | 中 | 低 |
| 無料枠 | **十分** | 制限あり | 申請必要 |

**推奨**: **Next.js + Vercel**での開発を採用。
- Vercelへのデプロイ経験が得られる
- モダンなフロントエンド開発スキルが身につく
- 本番URLをそのままデモに使用可能
- 無料枠で十分に動作

## 参考リンク

- [Next.js ドキュメント](https://nextjs.org/docs)
- [Vercel ドキュメント](https://vercel.com/docs)
- [Gemini API ドキュメント](https://ai.google.dev/docs)
- [Tailwind CSS](https://tailwindcss.com/docs)
