# Sonosei Text Crawler

listen.styleからテキストコンテンツをダウンロードするWebスクレイパーツール集

## 概要

このプロジェクトには3つのツールが含まれています：

1. **sonosei_crawler.py** - 基本的なHTTPリクエストベースのクローラー
2. **sonosei_crawler_selenium.py** - Seleniumを使用したブラウザ自動化版（より高度）
3. **sonosei_html_parser.py** - 保存したHTMLファイルからテキストを抽出

## 機能

- 指定されたURLからHTMLコンテンツを取得
- 記事、トランスクリプト、その他のテキストコンテンツを自動抽出
- 抽出したテキストをファイルに保存
- タイムスタンプ付きのファイル名で管理

## インストール

### 基本的な依存関係

```bash
pip install -r requirements.txt
```

### Selenium版を使用する場合

Seleniumを使用する場合は、ChromeとChromeDriverのインストールが必要です：

**Ubuntu/Debian:**
```bash
# Chromeのインストール
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb

# ChromeDriverのインストール
sudo apt install chromium-chromedriver
```

**macOS:**
```bash
brew install --cask google-chrome
brew install chromedriver
```

## 使い方

### 方法1: 基本的なクローラー（sonosei_crawler.py）

最もシンプルな方法ですが、一部のサイトでボット対策により403エラーが発生する可能性があります。

```bash
# デフォルトURLをクローリング
python sonosei_crawler.py

# カスタムURLを指定
python sonosei_crawler.py https://listen.style/p/sonosei/xfocemwo

# 出力ディレクトリを指定
python sonosei_crawler.py -o my_texts
```

### 方法2: Selenium版（sonosei_crawler_selenium.py）【推奨】

実際のブラウザを使用するため、より確実にコンテンツを取得できます。

```bash
# ヘッドレスモードで実行
python sonosei_crawler_selenium.py

# ブラウザを表示して実行（デバッグ用）
python sonosei_crawler_selenium.py --no-headless

# カスタムURLと出力ディレクトリを指定
python sonosei_crawler_selenium.py https://listen.style/p/sonosei/xfocemwo -o my_texts
```

### 方法3: 手動保存したHTMLからテキストを抽出（sonosei_html_parser.py）【最も確実】

ブラウザで手動でページを開き、「名前を付けて保存」→「ウェブページ、HTML のみ」で保存したファイルからテキストを抽出します。

```bash
# 保存したHTMLファイルを処理
python sonosei_html_parser.py page.html

# 出力ディレクトリを指定
python sonosei_html_parser.py page.html -o my_texts
```

**手順:**
1. ブラウザで対象ページを開く
2. 右クリック→「名前を付けて保存」（または Ctrl+S / Cmd+S）
3. 「ウェブページ、HTML のみ」を選択して保存
4. `python sonosei_html_parser.py 保存したファイル.html`を実行

## オプション

### sonosei_crawler.py / sonosei_crawler_selenium.py

- `url`: クローリング対象のURL（オプション、デフォルト: https://listen.style/p/sonosei/xfocemwo）
- `-o, --output`: 出力ディレクトリ（デフォルト: downloaded_texts）
- `--no-headless`: (Selenium版のみ) ブラウザを表示する

### sonosei_html_parser.py

- `html_file`: 入力HTMLファイルのパス（必須）
- `-o, --output`: 出力ディレクトリ（デフォルト: downloaded_texts）

## 出力

テキストファイルには以下の情報が含まれます:
- ページタイトル
- URL/ソースファイル
- 抽出日時
- 抽出されたテキストコンテンツ

ファイル名形式: `{タイトル}_{タイムスタンプ}.txt`

## トラブルシューティング

### 403 Forbidden エラーが発生する

- **解決策1**: Selenium版を使用してください
- **解決策2**: 手動でHTMLを保存し、HTMLパーサーを使用してください

### Seleniumでエラーが発生する

- ChromeとChromeDriverがインストールされているか確認
- バージョンの互換性を確認（Chromeとドライバーのバージョンが一致する必要があります）

### テキストが正しく抽出されない

- HTMLパーサー版を試してください（最も正確）
- 出力ファイルを確認し、必要に応じてセレクタを調整

## 注意事項

- Webスクレイピングを行う際は、対象サイトの利用規約を確認してください
- 過度なリクエストはサーバーに負荷をかける可能性があるため、適切な間隔でアクセスしてください
- このツールは個人的な利用を想定しています
- ボット対策が強力なサイトでは、手動保存 + HTMLパーサーの使用を推奨します
