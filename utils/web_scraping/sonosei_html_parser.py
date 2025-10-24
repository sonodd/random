#!/usr/bin/env python3
"""
Sonosei HTML Parser
保存したHTMLファイルからテキストコンテンツを抽出するツール
"""

import argparse
import os
from datetime import datetime
from pathlib import Path
from bs4 import BeautifulSoup


class HTMLTextExtractor:
    """HTMLファイルからテキストを抽出するクラス"""

    def __init__(self, html_file, output_dir="downloaded_texts"):
        """
        Args:
            html_file (str): 入力HTMLファイルのパス
            output_dir (str): テキストファイルの保存先ディレクトリ
        """
        self.html_file = html_file
        self.output_dir = output_dir

    def read_html(self):
        """HTMLファイルを読み込む"""
        try:
            with open(self.html_file, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print(f"Error: File not found: {self.html_file}")
            return None
        except Exception as e:
            print(f"Error reading file: {e}")
            return None

    def extract_text(self, html_content):
        """HTMLからテキストコンテンツを抽出"""
        soup = BeautifulSoup(html_content, 'html.parser')

        # タイトルを取得
        title = soup.find('title')
        title_text = title.get_text().strip() if title else "Untitled"

        # 不要なタグを削除
        for tag in soup(['script', 'style', 'nav', 'header', 'footer', 'aside', 'noscript', 'iframe']):
            tag.decompose()

        # メタ情報を収集
        meta_description = soup.find('meta', attrs={'name': 'description'})
        description = meta_description.get('content', '') if meta_description else ''

        og_title = soup.find('meta', attrs={'property': 'og:title'})
        og_title_text = og_title.get('content', '') if og_title else ''

        # テキストを抽出
        extracted_text = []
        extracted_text.append(f"Title: {title_text}")
        if og_title_text and og_title_text != title_text:
            extracted_text.append(f"OG Title: {og_title_text}")
        if description:
            extracted_text.append(f"Description: {description}")
        extracted_text.append(f"Source: {self.html_file}")
        extracted_text.append(f"Extracted on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        extracted_text.append("=" * 80)
        extracted_text.append("")

        # コンテンツを探す
        content_tags = []

        # 様々なセレクタを試す
        selectors = [
            'article',
            'main',
            '[role="main"]',
            '[class*="content"]',
            '[class*="post"]',
            '[class*="entry"]',
            '[class*="article"]',
            '[class*="text"]',
            '[id*="content"]',
            '[id*="main"]',
            '.post-content',
            '.article-content',
            '.entry-content'
        ]

        for selector in selectors:
            elements = soup.select(selector)
            if elements:
                content_tags.extend(elements)
                break

        # コンテンツが見つからない場合はbody全体を使用
        if not content_tags:
            body = soup.find('body')
            if body:
                content_tags = [body]

        # テキストを抽出
        seen_texts = set()

        for tag in content_tags:
            # 見出しと段落を取得
            for element in tag.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'li', 'blockquote', 'pre']):
                text = element.get_text().strip()

                # フィルタリング - 見出しとリストは短くても許可
                min_length = 5 if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li'] else 10

                if text and len(text) >= min_length:
                    # 重複を除外
                    if text not in seen_texts:
                        seen_texts.add(text)

                        # 見出しの場合は前後に空行を追加
                        if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                            extracted_text.append("")
                            extracted_text.append(text)
                            extracted_text.append("-" * min(len(text), 80))
                        elif element.name == 'li':
                            # リスト項目には箇条書き記号を追加
                            extracted_text.append(f"• {text}")
                        else:
                            extracted_text.append(text)

                        extracted_text.append("")

        return '\n'.join(extracted_text), title_text

    def save_text(self, text, title):
        """テキストをファイルに保存"""
        # 出力ディレクトリを作成
        Path(self.output_dir).mkdir(parents=True, exist_ok=True)

        # ファイル名を生成
        safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '-', '_')).strip()
        safe_title = safe_title[:100]

        if not safe_title:
            safe_title = "extracted_text"

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

    def process(self):
        """HTMLファイルを処理"""
        print(f"Processing HTML file: {self.html_file}")

        # HTMLを読み込む
        html_content = self.read_html()
        if not html_content:
            return False

        # テキストを抽出
        text, title = self.extract_text(html_content)

        if not text or len(text) < 100:
            print("Warning: Extracted text is very short or empty")

        # テキストを保存
        filepath = self.save_text(text, title)

        if filepath:
            print("Processing completed successfully!")
            return True
        else:
            print("Processing failed")
            return False


def main():
    """コマンドラインインターフェース"""
    parser = argparse.ArgumentParser(
        description='保存したHTMLファイルからテキストコンテンツを抽出'
    )
    parser.add_argument(
        'html_file',
        help='入力HTMLファイルのパス'
    )
    parser.add_argument(
        '-o', '--output',
        default='downloaded_texts',
        help='出力ディレクトリ (デフォルト: downloaded_texts)'
    )

    args = parser.parse_args()

    # パーサーを実行
    extractor = HTMLTextExtractor(args.html_file, args.output)
    success = extractor.process()

    return 0 if success else 1


if __name__ == '__main__':
    exit(main())
