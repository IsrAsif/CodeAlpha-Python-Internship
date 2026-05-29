# ============================================================
# TASK 3: Task Automation with Python Scripts
# Subtask  : Extract all email addresses from a .txt file
#            and save them to another file
# Intern   : Isra Asif  |  ID: CA/DF1/54477
# Internship: CodeAlpha — Python Programming (May 2026)
# ============================================================

import re
import os
from datetime import datetime


# ---------- 1. Configuration --------------------------------
# Change these paths to match your system
INPUT_FILE  = "input.txt"        # The .txt file to scan
OUTPUT_FILE = "extracted_emails.txt"  # Where to save found emails


# ---------- 2. Read input file ------------------------------
def read_file(filepath: str) -> str:
    if not os.path.exists(filepath):
        print(f"\n  ❌  File not found: '{filepath}'")
        print("  Please update INPUT_FILE in the script or place")
        print("  'input.txt' in the same folder as this script.\n")
        return None

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    print(f"\n  📄  Read file : '{filepath}'")
    print(f"      Size      : {len(content)} characters")
    return content


# ---------- 3. Extract emails using regex -------------------
def extract_emails(text: str) -> list:
    # Regex pattern — matches standard email formats
    pattern = r'[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}'
    emails = re.findall(pattern, text)

    # Remove duplicates while preserving order
    seen = set()
    unique_emails = []
    for email in emails:
        email_lower = email.lower()
        if email_lower not in seen:
            seen.add(email_lower)
            unique_emails.append(email)

    return unique_emails


# ---------- 4. Save emails to output file -------------------
def save_emails(emails: list, output_path: str) -> None:
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("EXTRACTED EMAIL ADDRESSES\n")
        f.write(f"Date      : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Source    : {INPUT_FILE}\n")
        f.write(f"Total     : {len(emails)} unique email(s)\n")
        f.write("=" * 45 + "\n\n")
        for i, email in enumerate(emails, 1):
            f.write(f"{i:>3}. {email}\n")

    print(f"\n  💾  Emails saved to: '{output_path}'\n")


# ---------- 5. Main -----------------------------------------
def main() -> None:
    print("\n" + "=" * 50)
    print("   📧  EMAIL EXTRACTOR — CodeAlpha Task 3")
    print("=" * 50)

    # Read input
    content = read_file(INPUT_FILE)
    if content is None:
        return

    # Extract
    emails = extract_emails(content)

    # Display results
    print(f"\n  🔍  Scanning for email addresses...\n")
    if not emails:
        print("  ⚠  No email addresses found in the file.\n")
        return

    print(f"  ✅  Found {len(emails)} unique email(s):\n")
    for i, email in enumerate(emails, 1):
        print(f"      {i:>3}. {email}")

    # Save to output file
    save_emails(emails, OUTPUT_FILE)

    print("  " + "-" * 48)
    print(f"  📊  Summary:")
    print(f"      Input file  : {INPUT_FILE}")
    print(f"      Output file : {OUTPUT_FILE}")
    print(f"      Emails found: {len(emails)}")
    print("  " + "-" * 48 + "\n")


if __name__ == "__main__":
    main()
