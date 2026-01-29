# 開発計画書

## 概要

| 項目 | 内容 |
|------|------|
| プロジェクト | AIチャットボット |
| 提出期限 | 2026年2月15日 23:59 |
| 開発期間 | 約3週間 |
| 技術スタック | Next.js 14 + TypeScript + Vercel + Gemini API |

---

## 開発フェーズ

```
┌─────────────────────────────────────────────────────────────────┐
│  Phase 1: MVP + Vercel初回デプロイ                               │
│  目標: 最小限動作するチャットボットをVercelにデプロイ           │
├─────────────────────────────────────────────────────────────────┤
│  Phase 2: 機能拡張                                               │
│  目標: RAG機能実装、講座内容への回答品質確保                    │
├─────────────────────────────────────────────────────────────────┤
│  Phase 3: 品質向上・動画作成                                     │
│  目標: テスト完了、デモ動画作成・提出                           │
└─────────────────────────────────────────────────────────────────┘
```

---

## Phase 1: MVP + Vercel初回デプロイ

### 目標
- 基本的なチャット機能が動作する
- Vercelにデプロイされ、URLでアクセス可能

### タスク一覧

| # | タスク | 成果物 | 完了条件 |
|---|--------|--------|---------|
| 1.1 | プロジェクト初期化 | Next.jsプロジェクト | `npm run dev` で起動確認 |
| 1.2 | Tailwind CSS設定 | スタイル設定ファイル | 基本スタイルが適用される |
| 1.3 | 環境変数設定 | .env.local, .env.example | APIキーが読み込まれる |
| 1.4 | Gemini APIクライアント実装 | `lib/gemini.ts` | TC-U-001 Pass |
| 1.5 | Chat API Route実装 | `app/api/chat/route.ts` | TC-I-001 Pass |
| 1.6 | チャットUIコンポーネント実装 | components/*.tsx | 入力・表示が動作 |
| 1.7 | メインページ統合 | `app/page.tsx` | ローカルでチャット動作 |
| 1.8 | Vercel初回デプロイ | 本番URL | URLでアクセス可能 |

### 詳細タスク

#### 1.1 プロジェクト初期化

```bash
npx create-next-app@latest chatbot --typescript --tailwind --app --src-dir
cd chatbot
npm install @google/generative-ai
```

#### 1.2 ディレクトリ構成作成

```
src/
├── app/
│   ├── page.tsx
│   ├── layout.tsx
│   ├── globals.css
│   └── api/chat/route.ts
├── components/
│   ├── ChatWindow.tsx
│   ├── ChatMessage.tsx
│   ├── ChatInput.tsx
│   └── LoadingSpinner.tsx
└── lib/
    ├── gemini.ts
    └── types.ts
```

#### 1.4 Gemini APIクライアント

```typescript
// lib/gemini.ts
import { GoogleGenerativeAI } from '@google/generative-ai';

const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY!);

export async function generateResponse(prompt: string): Promise<string> {
  const model = genAI.getGenerativeModel({ model: 'gemini-pro' });
  const result = await model.generateContent(prompt);
  return result.response.text();
}
```

#### 1.8 Vercelデプロイ

1. GitHubにpush
2. Vercelでリポジトリ接続
3. 環境変数 `GEMINI_API_KEY` 設定
4. デプロイ実行

### Phase 1 完了条件（品質ゲート）

- [ ] TC-U-001: Gemini API正常呼び出し Pass
- [ ] TC-U-002: APIキー未設定エラー Pass
- [ ] TC-I-001: POST /api/chat 正常系 Pass
- [ ] Vercel本番URLでチャット動作確認

---

## Phase 2: 機能拡張

### 目標
- RAG機能で講座内容を参照した回答が可能
- 講座関連質問（TC-Q-001〜004）に適切に回答

### タスク一覧

| # | タスク | 成果物 | 完了条件 |
|---|--------|--------|---------|
| 2.1 | 知識ベースドキュメント作成 | data/documents/*.md | 4ファイル作成 |
| 2.2 | RAGモジュール設計 | lib/rag/*.ts | 設計完了 |
| 2.3 | ドキュメントローダー実装 | lib/rag/loader.ts | TC-U-020 Pass |
| 2.4 | Retriever実装 | lib/rag/retriever.ts | TC-U-021 Pass |
| 2.5 | Chat APIにRAG統合 | api/chat/route.ts | TC-I-020, TC-I-021 Pass |
| 2.6 | 回答品質テスト | - | TC-Q-001〜004 Pass |
| 2.7 | UI改善（レスポンシブ） | components/*.tsx | モバイル対応 |
| 2.8 | 会話履歴機能 | - | TC-U-011, TC-E-002 Pass |

### 知識ベースドキュメント

| ファイル名 | 内容 | 対応テスト |
|-----------|------|-----------|
| colab_sft_guide.md | Google ColabでのSFT手順、T4制約 | TC-Q-001 |
| git_advanced.md | Git/GitHub応用テクニック | TC-Q-002 |
| llm_finetuning.md | ファインチューニング詳細 | TC-Q-003 |
| security_practices.md | セキュリティベストプラクティス | TC-Q-004 |

### RAG実装アプローチ

**シンプル版（推奨）**:
- ドキュメントをメモリに読み込み
- キーワードマッチングで関連ドキュメント取得
- プロンプトにコンテキストとして追加

```typescript
// 簡易RAG実装例
export function findRelevantContext(query: string): string {
  const documents = loadDocuments();
  const relevant = documents.filter(doc =>
    doc.keywords.some(kw => query.includes(kw))
  );
  return relevant.map(d => d.content).join('\n\n');
}
```

### Phase 2 完了条件（品質ゲート）

- [ ] TC-U-020: ドキュメント読み込み Pass
- [ ] TC-U-021: 類似ドキュメント検索 Pass
- [ ] TC-I-020: 知識ベース網羅性 Pass
- [ ] TC-I-021: コンテキスト取得精度 Pass
- [ ] TC-Q-001: Google Colab SFT制限 Pass
- [ ] TC-Q-002: Git/GitHub応用 Pass
- [ ] TC-Q-003: LLMファインチューニング Pass
- [ ] TC-Q-004: セキュリティベストプラクティス Pass

---

## Phase 3: 品質向上・動画作成

### 目標
- 全テストPass
- 提出用動画完成

### タスク一覧

| # | タスク | 成果物 | 完了条件 |
|---|--------|--------|---------|
| 3.1 | E2Eテスト実装・実行 | tests/e2e/*.ts | TC-E-001〜002 Pass |
| 3.2 | エラーハンドリング強化 | - | TC-E-003 Pass |
| 3.3 | ローディングUI改善 | - | UX向上 |
| 3.4 | 受け入れテスト実行 | - | TC-A-001〜004 Pass |
| 3.5 | デモシナリオ作成 | demo-script.md | シナリオ確定 |
| 3.6 | 動画撮影 | demo.mp4 | 約1分間 |
| 3.7 | 最終確認・提出 | - | 提出完了 |

### デモ動画シナリオ（案）

```
0:00 - 0:10  アプリ起動、UI紹介
0:10 - 0:25  基本チャット（挨拶）
0:25 - 0:45  講座関連質問（TC-Q-001: Colab SFT）
0:45 - 0:55  回答確認、RAG機能の説明
0:55 - 1:00  まとめ
```

### Phase 3 完了条件（最終ゲート）

- [ ] 全テストケース Pass
- [ ] デモ動画完成（約1分間）
- [ ] 動画内に講座関連質問を含む
- [ ] 期限内に提出完了

---

## リスクと対策

| リスク | 影響度 | 対策 |
|--------|--------|------|
| Gemini API無料枠超過 | 高 | 開発中はモック使用、本番テストは計画的に |
| RAG精度不足 | 中 | 知識ベースドキュメントを充実させる |
| Vercelデプロイ失敗 | 中 | 早期にデプロイ確認、ローカル動画も準備 |
| 時間不足 | 高 | Phase 1完了を最優先、RAGは簡易版で対応 |

---

## 優先順位

**必須（Must）**: Phase 1 全タスク
- これがないと提出要件を満たせない

**重要（Should）**: Phase 2 タスク 2.1, 2.5, 2.6
- 講座関連質問への回答品質確保

**あれば良い（Could）**: Phase 2 タスク 2.7, 2.8 / Phase 3 タスク 3.2, 3.3
- UX向上だが、なくても動作する

---

## 次のアクション

1. **Phase 1.1**: Next.jsプロジェクト初期化
2. **Phase 1.2**: Tailwind CSS設定
3. **Phase 1.3**: 環境変数設定
4. **Phase 1.4**: Gemini APIクライアント実装

開発を開始しますか？
