#!/usr/bin/env python3
"""
Sonosei Text Crawler (Selenium版)
listen.styleからテキストコンテンツをダウンロードするスクレイパー（ブラウザ自動化版）
"""

import argparse
import os
from datetime import datetime
from pathlib import Path
import time

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    SELENIUM_AVAILABLE = True
except ImportError:
    SELENIUM_AVAILABLE = False
    print("Warning: Selenium is not installed. Please install it with: pip install selenium")


class SonoseiCrawlerSelenium:
    """Seleniumを使用してlisten.styleのコンテンツをクローリングするクラス"""

    def __init__(self, url, output_dir="downloaded_texts", headless=True):
        """
        Args:
            url (str): クローリング対象のURL
            output_dir (str): テキストファイルの保存先ディレクトリ
            headless (bool): ヘッドレスモードで実行するか
        """
        if not SELENIUM_AVAILABLE:
            raise ImportError("Selenium is required. Install with: pip install selenium")

        self.url = url
        self.output_dir = output_dir
        self.headless = headless
        self.driver = None

    def setup_driver(self):
        """Chromeドライバーをセットアップ"""
        chrome_options = Options()

        if self.headless:
            chrome_options.add_argument('--headless')

        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
        chrome_options.add_argument('--lang=ja')

        try:
            self.driver = webdriver.Chrome(options=chrome_options)
            # WebDriver検出を回避
            self.driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
                'source': '''
                    Object.defineProperty(navigator, 'webdriver', {
                      get: () => undefined
                    })
                '''
            })
            return True
        except Exception as e:
            print(f"Error setting up Chrome driver: {e}")
            print("Make sure Chrome and ChromeDriver are installed.")
            return False

    def fetch_page(self):
        """URLからページを取得"""
        try:
            print(f"Fetching: {self.url}")
            self.driver.get(self.url)

            # ページの読み込みを待つ
            time.sleep(3)

            # ページタイトルを取得
            title = self.driver.title

            # ページのHTMLを取得
            html_content = self.driver.page_source

            return html_content, title
        except Exception as e:
            print(f"Error fetching page: {e}")
            return None, None

    def extract_text_from_html(self, html_content):
        """HTMLからテキストを抽出"""
        from bs4 import BeautifulSoup

        soup = BeautifulSoup(html_content, 'html.parser')

        # 不要なタグを削除
        for tag in soup(['script', 'style', 'nav', 'header', 'footer', 'aside', 'noscript']):
            tag.decompose()

        # テキストを抽出
        extracted_text = []

        # よくある記事コンテナを探す
        content_tags = []
        for selector in ['article', 'main', '[class*="content"]', '[class*="post"]',
                        '[class*="entry"]', '[class*="article"]', '[class*="text"]',
                        '[role="main"]']:
            elements = soup.select(selector)
            if elements:
                content_tags.extend(elements)
                break

        # コンテンツが見つからない場合はbody全体を使用
        if not content_tags:
            body = soup.find('body')
            if body:
                content_tags = [body]

        for tag in content_tags:
            # 段落やテキストブロックを取得
            paragraphs = tag.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'blockquote', 'div'])

            for p in paragraphs:
                text = p.get_text().strip()
                # 短すぎるテキストや重複を除外
                if text and len(text) > 15 and text not in extracted_text:
                    extracted_text.append(text)

        return '\n\n'.join(extracted_text)

    def save_text(self, text, title):
        """テキストをファイルに保存"""
        # 出力ディレクトリを作成
        Path(self.output_dir).mkdir(parents=True, exist_ok=True)

        # ファイル名を生成
        safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '-', '_')).strip()
        safe_title = safe_title[:100]

        if not safe_title:
            safe_title = "downloaded_text"

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{safe_title}_{timestamp}.txt"
        filepath = os.path.join(self.output_dir, filename)

        # メタデータを追加
        full_text = f"""Title: {title}
URL: {self.url}
Extracted on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
{'=' * 80}

{text}
"""

        # ファイルに書き込み
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(full_text)
            print(f"Text saved to: {filepath}")
            print(f"Total characters: {len(full_text)}")
            return filepath
        except IOError as e:
            print(f"Error saving file: {e}")
            return None

    def crawl(self):
        """クローリングを実行"""
        print("Starting Selenium crawl...")

        # ドライバーをセットアップ
        if not self.setup_driver():
            return False

        try:
            # ページを取得
            html_content, title = self.fetch_page()
            if not html_content:
                print("Failed to fetch page")
                return False

            # テキストを抽出
            text = self.extract_text_from_html(html_content)

            if not text or len(text) < 100:
                print("Warning: Extracted text is very short or empty")
                print(f"Extracted text length: {len(text)}")

            # テキストを保存
            filepath = self.save_text(text, title)

            if filepath:
                print("Crawl completed successfully!")
                return True
            else:
                print("Crawl failed")
                return False

        finally:
            # ドライバーを閉じる
            if self.driver:
                self.driver.quit()


def main():
    """コマンドラインインターフェース"""
    if not SELENIUM_AVAILABLE:
        print("Error: Selenium is not installed.")
        print("Please install it with: pip install selenium")
        return 1

    parser = argparse.ArgumentParser(
        description='listen.styleからテキストコンテンツをダウンロード (Selenium版)'
    )
    parser.add_argument(
        'url',
        nargs='?',
        default='https://listen.style/p/sonosei/xfocemwo',
        help='クローリング対象のURL (デフォルト: https://listen.style/p/sonosei/xfocemwo)'
    )
    parser.add_argument(
        '-o', '--output',
        default='downloaded_texts',
        help='出力ディレクトリ (デフォルト: downloaded_texts)'
    )
    parser.add_argument(
        '--no-headless',
        action='store_true',
        help='ヘッドレスモードを無効にする（ブラウザを表示）'
    )

    args = parser.parse_args()

    # クローラーを実行
    crawler = SonoseiCrawlerSelenium(
        args.url,
        args.output,
        headless=not args.no_headless
    )
    success = crawler.crawl()

    return 0 if success else 1


if __name__ == '__main__':
    exit(main())
