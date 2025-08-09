import sys
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
import validators
from urllib.parse import urljoin

# A4用紙1ページあたりの文字数目安
MAX_CHAR_COUNT = 1600
OUTPUT_FILENAME = "url_summarizer_summary.md"

def summarize_url(url: str):
    """
    URLを受け取り、そのページのコンテンツを要約してMarkdownファイルに出力する。
    """
    # URLのバリデーション
    if not validators.url(url):
        print(f"エラー: 無効なURLです - {url}")
        return

    try:
        # ページのHTMLを取得
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # HTTPエラーがあれば例外を発生させる
        response.encoding = response.apparent_encoding # 文字化け対策

        # BeautifulSoupでHTMLを解析
        soup = BeautifulSoup(response.text, 'html.parser')

        # タイトルを取得
        title = soup.title.string if soup.title else "タイトルなし"

        # メインコンテンツを抽出 (main, articleタグを優先)
        main_content = soup.find('main') or soup.find('article') or soup.body

        if main_content:
            # 不要なタグ（ヘッダー、フッター、ナビゲーションなど）を削除
            for tag in main_content.find_all(['header', 'footer', 'nav', 'aside', 'script', 'style']):
                tag.decompose()
            content_html = str(main_content)
        else:
            content_html = ""

        # HTMLをMarkdownに変換
        content_md = md(content_html).strip()

        # 文字数を制限
        if len(content_md) > MAX_CHAR_COUNT:
            content_md = content_md[:MAX_CHAR_COUNT] + "..."

        # リンクを収集
        links = []
        if main_content:
            for a_tag in main_content.find_all('a', href=True):
                link_url = a_tag['href']
                # 相対URLを絶対URLに変換
                absolute_url = urljoin(url, link_url)
                link_text = a_tag.get_text(strip=True)
                if link_text and absolute_url not in [l[1] for l in links]: # 重複を避ける
                    links.append((link_text, absolute_url))

        # Markdownファイルを生成
        with open(OUTPUT_FILENAME, "w", encoding="utf-8") as f:
            f.write(f"# {title}\n\n")
            f.write(f"**取得元URL:** {url}\n\n")
            f.write("## ページの概要\n\n")
            f.write(content_md + "\n\n")
            f.write("## ページ内の主要なリンク\n\n")
            if links:
                for text, link in links[:20]: # リンクの数を20に制限
                    f.write(f"- [{text}]({link})\n")
            else:
                f.write("リンクは見つかりませんでした。\n")

        print(f"サマリーが {OUTPUT_FILENAME} に保存されました。")

    except requests.exceptions.RequestException as e:
        print(f"エラー: ページを取得できませんでした。 {e}")
    except Exception as e:
        print(f"予期せぬエラーが発生しました: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"使い方: python {sys.argv[0]} <URL>")
        sys.exit(1)

    target_url = sys.argv[1]
    summarize_url(target_url)
