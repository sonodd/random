#!/usr/bin/env python3
"""
Sonosei Text Crawler
listen.styleからテキストコンテンツをダウンロードするスクレイパー
"""

import requests
from bs4 import BeautifulSoup
import argparse
import os
from datetime import datetime
from pathlib import Path


class SonoseiCrawler:
    """listen.styleのコンテンツをクローリングするクラス"""

    def __init__(self, url, output_dir="downloaded_texts"):
        """
        Args:
            url (str): クローリング対象のURL
            output_dir (str): テキストファイルの保存先ディレクトリ
        """
        self.url = url
        self.output_dir = output_dir
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'ja,en-US;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Cache-Control': 'max-age=0'
        })

    def fetch_page(self):
        """URLからHTMLを取得"""
        try:
            print(f"Fetching: {self.url}")
            response = self.session.get(self.url, timeout=30)
            response.raise_for_status()
            return response.content
        except requests.RequestException as e:
            print(f"Error fetching page: {e}")
            return None

    def extract_text(self, html_content):
        """HTMLからテキストコンテンツを抽出"""
        soup = BeautifulSoup(html_content, 'html.parser')

        # 不要なタグを削除
        for tag in soup(['script', 'style', 'nav', 'header', 'footer', 'aside']):
            tag.decompose()

        # メタデータを取得
        title = soup.find('title')
        title_text = title.get_text().strip() if title else "Untitled"

        # 本文を探す（一般的なコンテンツ要素）
        content_tags = []

        # よくある記事コンテナを探す
        for selector in ['article', 'main', '[class*="content"]', '[class*="post"]',
                        '[class*="entry"]', '[class*="article"]', '[class*="text"]']:
            elements = soup.select(selector)
            if elements:
                content_tags.extend(elements)

        # コンテンツが見つからない場合はbody全体を使用
        if not content_tags:
            body = soup.find('body')
            if body:
                content_tags = [body]

        # テキストを抽出
        extracted_text = []
        extracted_text.append(f"Title: {title_text}")
        extracted_text.append(f"URL: {self.url}")
        extracted_text.append(f"Extracted on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        extracted_text.append("-" * 80)
        extracted_text.append("")

        for tag in content_tags:
            # 段落やテキストブロックを取得
            paragraphs = tag.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'blockquote'])

            if paragraphs:
                for p in paragraphs:
                    text = p.get_text().strip()
                    if text and len(text) > 10:  # 短すぎるテキストは除外
                        extracted_text.append(text)
                        extracted_text.append("")
            else:
                # 段落が見つからない場合は全テキストを取得
                text = tag.get_text().strip()
                if text:
                    # 余分な空白を削除
                    lines = [line.strip() for line in text.split('\n') if line.strip()]
                    extracted_text.extend(lines)

        return '\n'.join(extracted_text), title_text

    def save_text(self, text, title):
        """テキストをファイルに保存"""
        # 出力ディレクトリを作成
        Path(self.output_dir).mkdir(parents=True, exist_ok=True)

        # ファイル名を生成（タイトルから安全なファイル名を作成）
        safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '-', '_')).strip()
        safe_title = safe_title[:100]  # 長すぎる場合は切り詰める

        if not safe_title:
            safe_title = "downloaded_text"

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{safe_title}_{timestamp}.txt"
        filepath = os.path.join(self.output_dir, filename)

        # ファイルに書き込み
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"Text saved to: {filepath}")
            print(f"Total characters: {len(text)}")
            return filepath
        except IOError as e:
            print(f"Error saving file: {e}")
            return None

    def crawl(self):
        """クローリングを実行"""
        print("Starting crawl...")

        # ページを取得
        html_content = self.fetch_page()
        if not html_content:
            print("Failed to fetch page")
            return False

        # テキストを抽出
        text, title = self.extract_text(html_content)

        if not text or len(text) < 100:
            print("Warning: Extracted text is very short or empty")

        # テキストを保存
        filepath = self.save_text(text, title)

        if filepath:
            print("Crawl completed successfully!")
            return True
        else:
            print("Crawl failed")
            return False


def main():
    """コマンドラインインターフェース"""
    parser = argparse.ArgumentParser(
        description='listen.styleからテキストコンテンツをダウンロード'
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

    args = parser.parse_args()

    # クローラーを実行
    crawler = SonoseiCrawler(args.url, args.output)
    success = crawler.crawl()

    return 0 if success else 1


if __name__ == '__main__':
    exit(main())
