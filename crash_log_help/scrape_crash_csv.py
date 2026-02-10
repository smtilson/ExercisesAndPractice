import csv
import os
import shutil
from datetime import datetime, timedelta
from typing import List, Optional, Tuple

MINUTES = 3

SCRIPT_DIR = os.path.dirname(__file__)
ORIGINAL_DIR = os.path.join(SCRIPT_DIR, "log/original_logs")
SCRAPED_DIR = os.path.join(SCRIPT_DIR, "log/scraped_logs")
WIN_DOCS = r"C:\Users\seant\OneDrive\Documents"
WSL_DOCS = "/mnt/c/Users/seant/OneDrive/Documents"
# Allow override via env var `HW_DOCS`; prefer WSL mount if present when not overridden.
SOURCE_DOCS = os.environ.get("HW_DOCS")
if not SOURCE_DOCS:
    if os.path.exists(WSL_DOCS):
        SOURCE_DOCS = WSL_DOCS
    elif os.path.exists(WIN_DOCS):
        SOURCE_DOCS = WIN_DOCS
    else:
        SOURCE_DOCS = WIN_DOCS
print(f"Documents source: {SOURCE_DOCS}")

os.makedirs(SCRAPED_DIR, exist_ok=True)




def parse_datetime(date_str: str, time_str: Optional[str] = None) -> datetime:
    """Parse HWInfo timestamps like '2.2.2026' + '13:6:34.241'."""
    if time_str:
        return datetime.strptime(f"{date_str} {time_str}", "%d.%m.%Y %H:%M:%S.%f")
    return datetime.strptime(date_str, "%d.%m.%Y %H:%M:%S.%f")


def find_column_indices(header: List[str]) -> Tuple[Optional[int], Optional[int]]:
    lowered = [h.strip().lower() for h in header]
    date_idx = None
    time_idx = None
    for i, h in enumerate(lowered):
        if h == "date":
            date_idx = i
        if h == "time":
            time_idx = i
    if date_idx is None:
        for i, h in enumerate(lowered):
            if "date" in h and ("time" in h or "/" in h or "timestamp" in h):
                date_idx = i
                time_idx = None
                break
    return date_idx, time_idx


def read_header_n_rows(path: str) -> Tuple[List[str], List[List[str]]]:
    with open(path, newline="", encoding="cp1252") as f:
        rows = list(csv.reader(f))
    if not rows:
        return [], []
    return rows[0], rows[1:]


def parse_rows(rows: List[List[str]], date_idx: int, time_idx: Optional[int]) -> List[Tuple[datetime, List[str]]]:
    parsed = []
    for row in rows:
        max_idx = date_idx if time_idx is None else max(date_idx, time_idx)
        if len(row) <= max_idx:
            continue

        date_val = row[date_idx].strip()
        time_val = row[time_idx].strip() if time_idx is not None else None

        if not date_val:
            continue
        if time_idx is not None and not time_val:
            continue

        try:
            ts = parse_datetime(date_val, time_val)
            parsed.append((ts, row))
        except ValueError:
            continue

    return parsed


def filter_tail(parsed: List[Tuple[datetime, List[str]]], minutes: int) -> List[List[str]]:
    if not parsed:
        return []
    end_time = parsed[-1][0]
    start_time = end_time - timedelta(minutes=minutes)
    return [r for t, r in parsed if t >= start_time]


def write_csv(path: str, header: List[str], rows: List[List[str]]) -> None:
    with open(path, "w", newline="", encoding="cp1252") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)


def process_file(in_path: str, out_path: str, minutes: int) -> None:
    header, rows = read_header_n_rows(in_path)
    if not header:
        print(f"Skipping {os.path.basename(in_path)}: empty file")
        return

    date_idx, time_idx = find_column_indices(header)
    if date_idx is None:
        print(f"Skipping {os.path.basename(in_path)}: no Date column found in header")
        return

    parsed = parse_rows(rows, date_idx, time_idx)
    if not parsed:
        print(f"No valid rows parsed for {os.path.basename(in_path)} — skipping")
        return

    filtered = filter_tail(parsed, minutes)
    write_csv(out_path, header, filtered)
    print(f"Wrote {len(filtered)} rows to {out_path}")


def get_original_files(directory: str) -> List[str]:
    files = []
    for fname in sorted(os.listdir(directory)):
        if fname.startswith("."):
            continue
        path = os.path.join(directory, fname)
        if os.path.isfile(path):
            files.append(path)
    return files


def sync_hwinfo_from_documents(src_dir: str, dest_dir: str) -> None:
    """Copy HWInfoLog CSV files from `src_dir` into `dest_dir` if missing."""
    if not os.path.isdir(src_dir):
        print(f"Documents path not found: {src_dir}")
        return

    for fname in sorted(os.listdir(src_dir)):
        low = fname.lower()
        if not low.startswith("hwinfolog") or not low.endswith(".csv"):
            continue
        src = os.path.join(src_dir, fname)
        if not os.path.isfile(src):
            continue
        dest = os.path.join(dest_dir, fname)
        if os.path.exists(dest):
            continue
        try:
            shutil.copy2(src, dest)
            print(f"Copied {fname} to {dest_dir}")
        except Exception as e:
            print(f"Failed to copy {fname}: {e}")


def main(minutes: int = 3) -> None:
    # ensure any HWInfoLogs CSVs present in Documents are copied to ORIGINAL_DIR
    sync_from_docs = True
    if sync_from_docs:
        sync_hwinfo_from_documents(SOURCE_DOCS, ORIGINAL_DIR)
    files = get_original_files(ORIGINAL_DIR)
    for in_path in files:
        base = os.path.splitext(os.path.basename(in_path))[0]
        out_path = os.path.join(SCRAPED_DIR, f"{base}_tail.csv")
        if os.path.exists(out_path):
            print(f"Skipping {os.path.basename(in_path)}: {os.path.basename(out_path)} already exists")
            continue
        process_file(in_path, out_path, minutes)


if __name__ == "__main__":
    main()

