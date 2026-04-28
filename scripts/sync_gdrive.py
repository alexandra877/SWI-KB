"""
Syncs files from a Google Drive shared folder into the local _raw/ directory,
converting everything to Markdown.

Required environment variables:
  GDRIVE_SERVICE_ACCOUNT_JSON  - Contents of the service account key JSON file
  GDRIVE_FOLDER_ID             - ID of the Drive folder (or shared drive root) to sync from

Optional environment variables:
  RAW_DIR          - Path to the _raw folder (default: _raw relative to repo root)
  GDRIVE_RECURSIVE - Set to "true" to recurse into subfolders (default: false)
"""

import csv
import io
import json
import os
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

import fitz  # pymupdf
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]

# Google Workspace formats: map to (export_mime, temp_extension)
GOOGLE_EXPORT = {
    "application/vnd.google-apps.document": (
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        ".docx",
    ),
    "application/vnd.google-apps.presentation": (
        "application/vnd.openxmlformats-officedocument.presentationml.presentation",
        ".pptx",
    ),
    "application/vnd.google-apps.spreadsheet": ("text/csv", ".csv"),
}

SKIP_MIME_PREFIXES = ("image/", "video/", "audio/")
SKIP_EXTENSIONS = {".zip", ".tar", ".gz", ".exe", ".bin"}


# ---------------------------------------------------------------------------
# Conversion helpers
# ---------------------------------------------------------------------------

def _pandoc(src: Path) -> str:
    result = subprocess.run(
        ["pandoc", str(src), "-t", "markdown", "--wrap=none"],
        capture_output=True, text=True, check=True,
    )
    return result.stdout


def _pdf_to_md(src: Path) -> str:
    doc = fitz.open(str(src))
    pages = []
    for i, page in enumerate(doc):
        text = page.get_text("text").strip()
        if text:
            pages.append(f"## Page {i + 1}\n\n{text}")
    doc.close()
    return "\n\n---\n\n".join(pages) + "\n"


def _csv_to_md(src: Path) -> str:
    rows = list(csv.reader(src.read_text(encoding="utf-8-sig").splitlines()))
    if not rows:
        return ""
    header = rows[0]
    lines = [
        "| " + " | ".join(header) + " |",
        "| " + " | ".join(["---"] * len(header)) + " |",
    ]
    for row in rows[1:]:
        # Pad short rows so column count matches header
        padded = row + [""] * (len(header) - len(row))
        lines.append("| " + " | ".join(padded[: len(header)]) + " |")
    return "\n".join(lines) + "\n"


def to_markdown(tmp: Path, original_mime: str) -> str:
    ext = tmp.suffix.lower()
    if ext in {".docx", ".odt", ".rtf", ".html", ".htm", ".pptx"}:
        return _pandoc(tmp)
    if ext == ".pdf" or original_mime == "application/pdf":
        return _pdf_to_md(tmp)
    if ext == ".csv":
        return _csv_to_md(tmp)
    if ext in {".md", ".txt"}:
        return tmp.read_text(encoding="utf-8", errors="replace")
    # Fallback: wrap raw text in a code block
    try:
        content = tmp.read_text(encoding="utf-8", errors="replace")
        return f"```\n{content}\n```\n"
    except Exception:
        return f"<!-- Could not convert {tmp.name} -->\n"


# ---------------------------------------------------------------------------
# Drive helpers
# ---------------------------------------------------------------------------

def build_service():
    key_json = os.environ.get("GDRIVE_SERVICE_ACCOUNT_JSON")
    if not key_json:
        sys.exit("ERROR: GDRIVE_SERVICE_ACCOUNT_JSON is not set.")
    creds = service_account.Credentials.from_service_account_info(
        json.loads(key_json), scopes=SCOPES
    )
    return build("drive", "v3", credentials=creds)


def list_files(service, folder_id: str, recursive: bool) -> list:
    results, page_token = [], None
    while True:
        resp = service.files().list(
            q=f"'{folder_id}' in parents and trashed = false",
            fields="nextPageToken, files(id, name, mimeType, modifiedTime)",
            pageToken=page_token,
            supportsAllDrives=True,
            includeItemsFromAllDrives=True,
        ).execute()
        for item in resp.get("files", []):
            if item["mimeType"] == "application/vnd.google-apps.folder":
                if recursive:
                    results.extend(list_files(service, item["id"], recursive=True))
            else:
                results.append(item)
        page_token = resp.get("nextPageToken")
        if not page_token:
            break
    return results


def download_bytes(service, file_meta: dict) -> tuple[bytes, str]:
    """Return (raw_bytes, temp_extension) for a Drive file."""
    mime = file_meta["mimeType"]

    if mime in GOOGLE_EXPORT:
        export_mime, ext = GOOGLE_EXPORT[mime]
        req = service.files().export_media(fileId=file_meta["id"], mimeType=export_mime)
    else:
        ext = Path(file_meta["name"]).suffix or ".bin"
        req = service.files().get_media(fileId=file_meta["id"], supportsAllDrives=True)

    buf = io.BytesIO()
    dl = MediaIoBaseDownload(buf, req)
    done = False
    while not done:
        _, done = dl.next_chunk()
    return buf.getvalue(), ext


def safe_stem(name: str) -> str:
    stem = Path(name).stem
    for ch in r'\/:*?"<>|':
        stem = stem.replace(ch, "_")
    return stem


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    folder_id = os.environ.get("GDRIVE_FOLDER_ID")
    if not folder_id:
        sys.exit("ERROR: GDRIVE_FOLDER_ID is not set.")

    raw_dir = Path(os.environ.get("RAW_DIR", Path(__file__).parent.parent / "_raw"))
    raw_dir.mkdir(parents=True, exist_ok=True)
    recursive = os.environ.get("GDRIVE_RECURSIVE", "false").lower() == "true"

    service = build_service()
    print(f"Listing Drive folder {folder_id} (recursive={recursive})…")
    files = list_files(service, folder_id, recursive)
    print(f"Found {len(files)} file(s).\n")

    added = updated = skipped = errors = 0

    for f in files:
        mime = f["mimeType"]

        # Skip binary formats we can't usefully convert
        if any(mime.startswith(p) for p in SKIP_MIME_PREFIXES):
            print(f"  [skip] {f['name']} (unsupported type: {mime})")
            skipped += 1
            continue
        if Path(f["name"]).suffix.lower() in SKIP_EXTENSIONS:
            print(f"  [skip] {f['name']} (unsupported extension)")
            skipped += 1
            continue

        dest = raw_dir / (safe_stem(f["name"]) + ".md")
        drive_mtime = datetime.fromisoformat(f["modifiedTime"].replace("Z", "+00:00"))

        if dest.exists():
            local_mtime = datetime.fromtimestamp(dest.stat().st_mtime, tz=timezone.utc)
            if local_mtime >= drive_mtime:
                skipped += 1
                continue
            action = "updated"
        else:
            action = "added"

        try:
            raw_bytes, tmp_ext = download_bytes(service, f)
            with tempfile.NamedTemporaryFile(suffix=tmp_ext, delete=False) as tmp_file:
                tmp_path = Path(tmp_file.name)
                tmp_file.write(raw_bytes)

            md_content = to_markdown(tmp_path, mime)
            tmp_path.unlink(missing_ok=True)

            dest.write_text(md_content, encoding="utf-8")
            print(f"  [{action}] {dest.name}")
            if action == "added":
                added += 1
            else:
                updated += 1

        except Exception as e:
            print(f"  [error] {f['name']}: {e}", file=sys.stderr)
            errors += 1

    print(f"\nDone — added: {added}, updated: {updated}, skipped: {skipped}, errors: {errors}")
    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
