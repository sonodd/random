# コントリビューションガイド

このリポジトリにコードを追加する際のルールとガイドラインです。

## 基本方針

- **Publicリポジトリ**として運用しています
- 機能確認・テスト開発用のコードを集めています
- 外部に公開できる情報のみを含めてください

---

## セキュリティチェックリスト

コードを追加する前に、以下を必ず確認してください。

### 必須確認項目

- [ ] APIキー・パスワードがハードコードされていない
- [ ] 個人情報を含むデータが含まれていない
- [ ] 認証情報が環境変数または外部設定ファイルで管理されている
- [ ] 著作権のあるデータ・コードを使用していない（または許諾済み）
- [ ] 機密性の高いログ出力がない

### APIキーの扱い方

**NG例（絶対にしないでください）:**
```python
api_key = "sk-xxxxxxxxxxxxxxxxxxxx"
```

**OK例:**
```python
# 環境変数から取得
import os
api_key = os.getenv('OPENAI_API_KEY')

# Google Colabの場合
from google.colab import userdata
api_key = userdata.get('OPENAI_API_KEY')
```

---

## ディレクトリ構成

新しいプロジェクトは、適切なカテゴリのディレクトリに配置してください。

```
random/
├── ai-ml/              # AI・機械学習関連
├── data-analysis/      # データ分析
├── algorithms/         # アルゴリズム・ロジック
└── web/                # Web関連（API、スクレイピング等）
```

### 新しいカテゴリが必要な場合

既存のカテゴリに当てはまらない場合は、新しいカテゴリを作成できます。

```
random/
├── (既存カテゴリ)
└── new-category/       # 新しいカテゴリ
    └── project-name/
```

---

## プロジェクト構成

各プロジェクトには以下のファイルを含めてください。

```
category/project-name/
├── README.md           # 必須：プロジェクトの説明
├── requirements.txt    # 推奨：依存ライブラリ（Pythonの場合）
├── main.py または *.ipynb
└── sample_data/        # 任意：サンプルデータ
```

### README.mdテンプレート

```markdown
# プロジェクト名

簡潔な説明（1-2文）

## 概要

このプロジェクトの目的と内容

## 機能

- 機能1
- 機能2

## 必要な環境

- Python 3.8+
- その他の要件

## 依存ライブラリ

```
library1
library2
```

## 使い方

1. ステップ1
2. ステップ2

## ファイル構成

```
project-name/
├── README.md
└── main.py
```
```

---

## コミットルール

### コミットメッセージの形式

```
<type>(<scope>): <subject>
```

**Type:**
- `feat`: 新機能追加
- `fix`: バグ修正
- `docs`: ドキュメントのみの変更
- `refactor`: リファクタリング
- `test`: テストの追加・修正

**Scope:**
- カテゴリ名またはプロジェクト名

**例:**
```
feat(ai-ml): OpenAI APIでテキスト分類を実装
fix(web): スクレイピングのエンコードエラーを修正
docs: READMEにセットアップ手順を追加
refactor(algorithms): コードの可読性を改善
```

### コミット前の確認

```bash
# 差分を確認
git diff --staged

# 機密情報が含まれていないか確認
git diff --staged | grep -E "(api_key|password|secret|token)"
```

---

## ルートREADMEの更新

新しいプロジェクトを追加したら、`README.md`の「プロジェクト一覧」を更新してください。

```markdown
| [category/project-name](./category/project-name/) | プロジェクトの説明 | ステータス |
```

**ステータス:**
- `✅ 動作確認済` - テスト完了
- `🚧 開発中` - 作業中
- `⚠️ 要修正` - 問題あり

---

## コーディング規約

### Python

- [PEP 8](https://pep8-ja.readthedocs.io/) に準拠
- 変数名・関数名は英語（snake_case）
- コメントは日本語OK

### Jupyter Notebook

- セルの出力はクリアしてからコミット（メタデータ削減）
- マークダウンセルで説明を追加

---

## 禁止事項

以下の内容は絶対に含めないでください。

- APIキー、パスワード、トークン
- 個人情報（氏名、メールアドレス、住所等）
- 企業の機密情報
- 著作権を侵害するコンテンツ
- マルウェアや悪意のあるコード

---

## 質問・相談

不明な点があれば、Issueを作成してください。
