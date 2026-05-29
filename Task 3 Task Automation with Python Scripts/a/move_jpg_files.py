# ============================================================
# TASK 3: Task Automation with Python Scripts
# Subtask  : Move all .jpg files from a folder to a new folder
# Intern   : Isra Asif  |  ID: CA/DF1/54477
# Internship: CodeAlpha — Python Programming (May 2026)
# ============================================================

import os
import shutil
from datetime import datetime


# ---------- 1. Configuration --------------------------------
# Change these two paths to match your system
SOURCE_FOLDER = r"C:\Users\Name\Pictures"          # Folder to search in
DESTINATION_FOLDER = r"C:\Users\Name\Pictures\JPG_Moved"  # Folder to move to


# ---------- 2. Move JPG files -------------------------------
def move_jpg_files(source: str, destination: str) -> None:

    print("\n" + "=" * 50)
    print("   🗂  JPG FILE MOVER — CodeAlpha Task 3")
    print("=" * 50)

    # --- Validate source folder ---
    if not os.path.exists(source):
        print(f"\n  ❌  Source folder not found:\n     {source}")
        print("  Please update SOURCE_FOLDER in the script.\n")
        return

    # --- Create destination folder if it doesn't exist ---
    if not os.path.exists(destination):
        os.makedirs(destination)
        print(f"\n  📁  Created destination folder:\n     {destination}")
    else:
        print(f"\n  📁  Destination folder already exists:\n     {destination}")

    # --- Find all .jpg / .jpeg files in source folder ---
    jpg_files = [
        f for f in os.listdir(source)
        if f.lower().endswith((".jpg", ".jpeg"))
        and os.path.isfile(os.path.join(source, f))
    ]

    if not jpg_files:
        print(f"\n  ⚠  No .jpg files found in:\n     {source}\n")
        return

    print(f"\n  Found {len(jpg_files)} .jpg file(s) to move:\n")

    moved = 0
    skipped = 0
    log_lines = []

    for filename in jpg_files:
        src_path = os.path.join(source, filename)
        dst_path = os.path.join(destination, filename)

        # --- Handle duplicate filenames ---
        if os.path.exists(dst_path):
            name, ext = os.path.splitext(filename)
            timestamp = datetime.now().strftime("%H%M%S")
            new_filename = f"{name}_{timestamp}{ext}"
            dst_path = os.path.join(destination, new_filename)
            print(f"  ⚠  Duplicate found — renaming to: {new_filename}")

        try:
            shutil.move(src_path, dst_path)
            final_name = os.path.basename(dst_path)
            print(f"  ✅  Moved: {filename}")
            log_lines.append(f"MOVED   | {filename} -> {final_name}")
            moved += 1
        except Exception as e:
            print(f"  ❌  Failed to move {filename}: {e}")
            log_lines.append(f"FAILED  | {filename} | Error: {e}")
            skipped += 1

    # ---------- 3. Summary ----------------------------------
    print("\n" + "-" * 50)
    print(f"  📊  Summary:")
    print(f"      ✅  Moved   : {moved} file(s)")
    print(f"      ⚠  Skipped : {skipped} file(s)")
    print(f"      📂  Saved to: {destination}")
    print("-" * 50)

    # ---------- 4. Save log file ----------------------------
    log_path = os.path.join(destination, "move_log.txt")
    with open(log_path, "w") as log_file:
        log_file.write("JPG FILE MOVER — LOG\n")
        log_file.write(f"Date     : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        log_file.write(f"Source   : {source}\n")
        log_file.write(f"Dest     : {destination}\n")
        log_file.write("=" * 45 + "\n")
        for line in log_lines:
            log_file.write(line + "\n")
        log_file.write("=" * 45 + "\n")
        log_file.write(f"Total moved  : {moved}\n")
        log_file.write(f"Total skipped: {skipped}\n")

    print(f"\n  💾  Log saved to: {log_path}\n")


# ---------- 5. Main -----------------------------------------
if __name__ == "__main__":
    move_jpg_files(SOURCE_FOLDER, DESTINATION_FOLDER)
