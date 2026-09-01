from __future__ import annotations

import csv
import hashlib
import json
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "project" / "Pompa_Air_LAD_V16.zap16"
FB_XML = ROOT / "source" / "FB_PumpControl_LAD.xml"
MAIN_XML = ROOT / "source" / "Main_LAD.xml"
IO_XML = ROOT / "source" / "Pump_IO_LAD.xml"
IO_CSV = ROOT / "docs" / "IO_List.csv"
MANIFEST = ROOT / "validation" / "delivery_manifest.json"

EXPECTED_ARCHIVE_SHA256 = "65a72e13ff16726609517d6af1e0a326627a98e8f811c0ebe68291ef2cf5d25f"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    required = [ARCHIVE, FB_XML, MAIN_XML, IO_XML, IO_CSV, MANIFEST]
    missing = [str(path.relative_to(ROOT)) for path in required if not path.is_file()]
    if missing:
        fail(f"missing files: {', '.join(missing)}")

    archive_hash = sha256(ARCHIVE)
    if archive_hash != EXPECTED_ARCHIVE_SHA256:
        fail(f"archive SHA-256 mismatch: {archive_hash}")

    with zipfile.ZipFile(ARCHIVE) as archive:
        bad_entry = archive.testzip()
        entry_count = len(archive.infolist())
    if bad_entry is not None:
        fail(f"archive CRC error: {bad_entry}")
    if entry_count != 60:
        fail(f"expected 60 archive entries, found {entry_count}")

    fb_tree = ET.parse(FB_XML)
    networks = sum(1 for node in fb_tree.iter() if node.tag.endswith("SW.Blocks.CompileUnit"))
    if networks != 53:
        fail(f"expected 53 LAD networks, found {networks}")

    ET.parse(MAIN_XML)
    ET.parse(IO_XML)

    with IO_CSV.open(encoding="utf-8-sig", newline="") as handle:
        io_rows = list(csv.DictReader(handle))
    if len(io_rows) != 13:
        fail(f"expected 13 I/O rows, found {len(io_rows)}")

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    compile_result = manifest["tia_compile"]["software_rebuild_all"]
    if compile_result != {"errors": 0, "warnings": 0}:
        fail(f"unexpected TIA compile result: {compile_result}")

    print("PASS")
    print(f"Archive SHA-256 : {archive_hash}")
    print(f"Archive entries : {entry_count}, CRC OK")
    print(f"LAD networks    : {networks}")
    print(f"I/O tags        : {len(io_rows)}")
    print("TIA compile     : 0 errors, 0 warnings")


if __name__ == "__main__":
    main()

