# AI チャットボット

講座最終課題として開発するAIチャットボットプロジェクト。

## 概要

Gemini APIを活用したWebベースのAIチャットボット。
**Next.js + Vercel** で構築し、本番環境へのデプロイまで行う。

## プロジェクト構成

```
chatbot/
├── docs/                    # 設計ドキュメント
│   ├── requirements.md     # 要件定義書
│   ├── design.md           # システム設計書
│   ├── architecture.md     # アーキテクチャ設計書
│   └── testing.md          # テスト仕様書
├── src/                     # ソースコード（実装時に作成）
│   ├── app/                # Next.js App Router
│   ├── components/         # Reactコンポーネント
│   └── lib/                # ユーティリティ
├── tests/                   # テストコード（実装時に作成）
└── README.md               # このファイル
```

## 技術スタック

| カテゴリ | 技術 |
|----------|------|
| LLM API | Google Gemini API |
| フレームワーク | Next.js 14 (App Router) |
| 言語 | TypeScript |
| UI | React + Tailwind CSS |
| デプロイ | **Vercel** (Hobby Plan) |

## クイックスタート

### 前提条件

- Node.js 18以上
- npm または yarn
- Gemini API キー

### セットアップ

```bash
# リポジトリをクローン
git clone <repository-url>
cd chatbot

# 依存関係をインストール
npm install

# 環境変数を設定
cp .env.example .env.local
# .env.local を編集して GEMINI_API_KEY を設定
```

### ローカル実行

```bash
npm run dev
```

ブラウザで `http://localhost:3000` を開く。

### Vercelへデプロイ

1. [Vercel](https://vercel.com) にサインアップ
2. GitHubリポジトリを接続
3. 環境変数 `GEMINI_API_KEY` を設定
4. デプロイ実行（自動）

## 開発スケジュール

| フェーズ | 内容 | 期間 |
|---------|------|------|
| Phase 1 | MVP + Vercel初回デプロイ | Week 1 |
| Phase 2 | 機能拡張・UI改善 | Week 2 |
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
- [テスト仕様書](docs/testing.md) - テストケース・テスト計画
- [開発計画書](docs/development-plan.md) - フェーズ別タスク・スケジュール

## ライセンス

Private - 講座課題用
