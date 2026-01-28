# システム設計書

## 概要

本ドキュメントでは、AIチャットボットシステムの詳細設計を記述する。

## システム構成

### コンポーネント構成

```
┌─────────────────────────────────────────────────────────────┐
│                      Client (Browser)                        │
│  ┌─────────────────────────────────────────────────────┐    │
│  │                  Chat UI Component                   │    │
│  │  ・メッセージ入力フォーム                            │    │
│  │  ・会話履歴表示                                      │    │
│  │  ・ローディング状態表示                              │    │
│  └─────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Backend Server                            │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  API Router  │→│ Chat Service │→│ LLM Client   │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│                              │                               │
│                              ▼                               │
│                    ┌──────────────┐                         │
│                    │  RAG Module  │ (optional)              │
│                    │  ・Embedding │                         │
│                    │  ・Vector DB │                         │
│                    └──────────────┘                         │
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

## モジュール設計

### 1. Chat UI Component

**責務**: ユーザーインターフェースの提供

| 機能 | 説明 |
|------|------|
| メッセージ入力 | テキスト入力フォーム、送信ボタン |
| 会話表示 | ユーザー/AI メッセージの表示 |
| 状態管理 | ローディング、エラー状態の表示 |

**インターフェース**:
```typescript
interface Message {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  timestamp: Date;
}

interface ChatState {
  messages: Message[];
  isLoading: boolean;
  error: string | null;
}
```

### 2. API Router

**責務**: HTTPリクエストのルーティング

| エンドポイント | メソッド | 説明 |
|---------------|----------|------|
| `/api/chat` | POST | チャットメッセージの送信 |
| `/api/health` | GET | ヘルスチェック |

**リクエスト/レスポンス形式**:
```typescript
// POST /api/chat
interface ChatRequest {
  message: string;
  conversationHistory?: Message[];
}

interface ChatResponse {
  response: string;
  conversationId?: string;
}
```

### 3. Chat Service

**責務**: チャットロジックの処理

| 機能 | 説明 |
|------|------|
| メッセージ処理 | ユーザー入力の前処理 |
| コンテキスト管理 | 会話履歴の管理 |
| プロンプト構築 | LLMに送信するプロンプトの生成 |

### 4. LLM Client

**責務**: Gemini APIとの通信

| 機能 | 説明 |
|------|------|
| API呼び出し | Gemini APIへのリクエスト送信 |
| エラーハンドリング | API エラーの処理 |
| レート制限対応 | 無料枠内での利用管理 |

**設定**:
```typescript
interface LLMConfig {
  apiKey: string;
  model: 'gemini-pro' | 'gemini-pro-vision';
  maxTokens: number;
  temperature: number;
}
```

### 5. RAG Module（オプション）

**責務**: 外部知識の検索と統合

| サブモジュール | 説明 |
|---------------|------|
| Document Loader | ドキュメントの読み込み |
| Text Splitter | テキストのチャンク分割 |
| Embedding | テキストのベクトル化 |
| Vector Store | ベクトルの保存・検索 |
| Retriever | 関連ドキュメントの取得 |

## データフロー

### 基本チャットフロー

```
1. ユーザーがメッセージを入力
2. Chat UI → API Router: POST /api/chat
3. API Router → Chat Service: メッセージ処理
4. Chat Service → LLM Client: プロンプト送信
5. LLM Client → Gemini API: API呼び出し
6. Gemini API → LLM Client: 応答受信
7. LLM Client → Chat Service: 応答処理
8. Chat Service → API Router: レスポンス生成
9. API Router → Chat UI: JSON レスポンス
10. Chat UI: 応答を表示
```

### RAG 統合フロー

```
1. ユーザーがメッセージを入力
2. Chat Service → RAG Module: クエリ送信
3. RAG Module → Embedding: クエリをベクトル化
4. RAG Module → Vector Store: 類似ドキュメント検索
5. RAG Module → Chat Service: 関連コンテキスト返却
6. Chat Service: プロンプトにコンテキストを追加
7. （以降は基本フローと同様）
```

## エラーハンドリング

| エラー種別 | 対応 |
|-----------|------|
| API接続エラー | リトライ（最大3回）後、ユーザーに通知 |
| レート制限 | 待機後リトライ、ユーザーに待機を通知 |
| 入力バリデーションエラー | 即時エラーメッセージ表示 |
| 内部サーバーエラー | 汎用エラーメッセージ表示、ログ記録 |

## セキュリティ設計

### APIキー管理

```
環境変数: GEMINI_API_KEY
└── .env ファイル（.gitignore に追加）
└── 本番環境: 環境変数として設定
```

### 入力検証

| 項目 | 対策 |
|------|------|
| XSS | 入力のサニタイズ、出力のエスケープ |
| プロンプトインジェクション | 入力長制限、危険パターンのフィルタリング |

## テスト戦略

| テスト種別 | 対象 | ツール |
|-----------|------|--------|
| ユニットテスト | 各モジュール | Jest / pytest |
| 統合テスト | API エンドポイント | Supertest / httpx |
| E2Eテスト | ユーザーフロー | Playwright / Cypress |
