"""Build a reproducible ZIP archive and SHA-256 checksum for a data release.

The archive contains every file tracked by Git at the checked-out release
commit. Fixed ZIP timestamps, sorted entries and explicit file modes make the
same commit produce the same archive, which keeps release checksums meaningful.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

TOKEN_PATTERN = re.compile(r"[^A-Za-z0-9._-]+")
ZIP_TIMESTAMP = (1980, 1, 1, 0, 0, 0)
ZIP_FILE_MODE = 0o644
ZIP_EXECUTABLE_MODE = 0o755
DEFAULT_ARCHIVE_NAME = "data-release"
_GIT = shutil.which("git")


def git_files() -> list[tuple[str, int]]:
    """Return tracked files and their executable bits from the current commit."""
    if _GIT is None:
        raise RuntimeError("git is required to build a release archive")
    result = subprocess.run(  # noqa: S603 - _GIT is resolved with shutil.which.
        [_GIT, "ls-files", "-z"], check=True, capture_output=True, text=False
    )
    files = []
    for raw_name in result.stdout.split(b"\0"):
        if not raw_name:
            continue
        name = raw_name.decode("utf-8")
        mode = subprocess.run(  # noqa: S603 - _GIT is resolved with shutil.which.
            [_GIT, "ls-files", "-s", "--", name], check=True, capture_output=True, text=True
        ).stdout.split()[0]
        files.append((name, int(mode, 8)))
    return files


def archive_name(value: str) -> str:
    """Make a user-provided archive name safe and stable."""
    cleaned = TOKEN_PATTERN.sub("-", value).strip("-.")
    if not cleaned:
        raise ValueError("archive name must contain at least one safe character")
    return cleaned


def build_archive(output_dir: Path, name: str) -> tuple[Path, Path]:
    """Build a deterministic archive and its checksum."""
    output_dir.mkdir(parents=True, exist_ok=True)
    archive = output_dir / f"{archive_name(name)}.zip"
    checksum = output_dir / f"{archive.stem}.sha256"
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as result:
        for filename, mode in git_files():
            source = Path(filename)
            if not source.is_file():
                continue
            info = zipfile.ZipInfo(filename, ZIP_TIMESTAMP)
            info.create_system = 3
            info.external_attr = ((ZIP_EXECUTABLE_MODE if mode & 0o111 else ZIP_FILE_MODE) & 0xFFFF) << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            result.writestr(info, source.read_bytes())
    checksum.write_text(f"{hashlib.sha256(archive.read_bytes()).hexdigest()}  {archive.name}\n", encoding="utf-8")
    return archive, checksum


def main() -> int:
    """Build an archive from the checked-out Git tree."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=Path("dist"))
    parser.add_argument("--name", default=DEFAULT_ARCHIVE_NAME)
    args = parser.parse_args()
    archive, checksum = build_archive(args.output_dir, args.name)
    print(f"Created {archive} and {checksum}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
