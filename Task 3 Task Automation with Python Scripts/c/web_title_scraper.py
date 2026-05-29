# ============================================================
# TASK 3: Task Automation with Python Scripts
# Subtask  : Scrape the title of a fixed webpage and save it
# Intern   : Isra Asif  |  ID: CA/DF1/54477
# Internship: CodeAlpha — Python Programming (May 2026)
# ============================================================

import requests
import re
import os
from datetime import datetime


# ---------- 1. Configuration --------------------------------
# The fixed webpage to scrape
URL = "https://www.wikipedia.org"

# Output file to save the title
OUTPUT_FILE = "scraped_title.txt"


# ---------- 2. Fetch webpage content ------------------------
def fetch_page(url: str) -> str:
    print(f"\n  🌐  Fetching webpage: {url}")

    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()   # Raises error for 4xx/5xx status codes
        print(f"  ✅  Status Code : {response.status_code} OK")
        return response.text

    except requests.exceptions.ConnectionError:
        print("  ❌  Connection failed. Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("  ❌  Request timed out. The website took too long to respond.")
    except requests.exceptions.HTTPError as e:
        print(f"  ❌  HTTP Error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"  ❌  Unexpected error: {e}")

    return None


# ---------- 3. Extract title using regex --------------------
def extract_title(html: str) -> str:
    # Regex to find content inside <title>...</title>
    match = re.search(r'<title[^>]*>(.*?)</title>', html, re.IGNORECASE | re.DOTALL)

    if match:
        # Clean up whitespace and HTML entities
        title = match.group(1).strip()
        title = title.replace("&amp;", "&")
        title = title.replace("&lt;", "<")
        title = title.replace("&gt;", ">")
        title = title.replace("&quot;", '"')
        title = title.replace("&#39;", "'")
        return title

    return None


# ---------- 4. Save result to file --------------------------
def save_title(url: str, title: str, output_path: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Append to file so multiple runs are recorded
    mode = "a" if os.path.exists(output_path) else "w"

    with open(output_path, mode, encoding="utf-8") as f:
        f.write("=" * 45 + "\n")
        f.write(f"Date   : {timestamp}\n")
        f.write(f"URL    : {url}\n")
        f.write(f"Title  : {title}\n")
        f.write("=" * 45 + "\n\n")

    print(f"\n  💾  Title saved to: '{output_path}'")


# ---------- 5. Main -----------------------------------------
def main() -> None:
    print("\n" + "=" * 50)
    print("   🔍  WEB TITLE SCRAPER — CodeAlpha Task 3")
    print("=" * 50)

    # Fetch page
    html = fetch_page(URL)
    if html is None:
        return

    # Extract title
    title = extract_title(html)

    if not title:
        print("\n  ⚠  Could not find a <title> tag on the page.\n")
        return

    print(f"\n  📄  Page Title Found:")
    print(f"      \"{title}\"")

    # Save to file
    save_title(URL, title, OUTPUT_FILE)

    # Summary
    print("\n  " + "-" * 46)
    print(f"  📊  Summary:")
    print(f"      URL         : {URL}")
    print(f"      Title       : {title}")
    print(f"      Saved to    : {OUTPUT_FILE}")
    print(f"      Timestamp   : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("  " + "-" * 46 + "\n")


if __name__ == "__main__":
    main()
