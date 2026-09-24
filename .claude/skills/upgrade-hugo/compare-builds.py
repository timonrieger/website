#!/usr/bin/env python3
"""Group every difference between two Hugo build outputs.

Usage: compare-builds.py BEFORE_DIR AFTER_DIR
"""

import hashlib
import re
import sys
from collections import defaultdict
from difflib import unified_diff
from pathlib import Path

BINARY = {".png", ".jpg", ".jpeg", ".webp", ".avif", ".ico", ".gif", ".pdf", ".woff2"}
norm = lambda s: re.sub(r"_hu_[0-9a-f]+", "_hu_HASH", s)
digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()


def main(before: Path, after: Path) -> int:
    files = lambda root: {
        norm(str(p.relative_to(root))): p for p in root.rglob("*") if p.is_file()
    }
    b, a = files(before), files(after)

    for label, missing in (
        ("only before", b.keys() - a.keys()),
        ("only after", a.keys() - b.keys()),
    ):
        for rel in sorted(missing):
            print(f"[{label}] {rel}")

    img = lambda m: sorted(
        digest(p) for rel, p in m.items() if Path(rel).suffix.lower() in BINARY
    )
    print(
        f"[images] bytes {'identical' if img(b) == img(a) else 'DIFFER'} on both sides"
    )

    groups = defaultdict(list)
    for rel in sorted(b.keys() & a.keys()):
        if Path(rel).suffix.lower() in BINARY:
            continue
        try:
            tb, ta = norm(b[rel].read_text()), norm(a[rel].read_text())
        except UnicodeDecodeError:
            continue
        if tb == ta:
            continue
        split = lambda s: re.split(r"(?=<)", s) if "<" in s[:200] else s.split("\n")
        diff = [
            l
            for l in unified_diff(split(tb), split(ta), lineterm="", n=0)
            if l[:1] in "+-" and not l.startswith(("---", "+++"))
        ]
        groups[tuple(sorted({l[:120] for l in diff}))].append(rel)

    print(
        f"[text] {sum(len(v) for v in groups.values())} files differ in {len(groups)} shapes"
    )
    for shape, rels in sorted(groups.items(), key=lambda kv: -len(kv[1])):
        print(f"\n[{len(rels)}] {', '.join(rels[:3])}{' …' if len(rels) > 3 else ''}")
        for line in shape:
            print(f"    {line}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    sys.exit(main(Path(sys.argv[1]), Path(sys.argv[2])))
