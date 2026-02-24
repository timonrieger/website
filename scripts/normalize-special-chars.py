# /// script
# requires-python = ">=3.9"
# description = "Normalize smart quotes and special punctuation in Markdown files."
# ///


import sys
from pathlib import Path

REPLACEMENTS = {
    "'": "'",
    "'": "'",  # noqa F601
    """: '"',
    """: '"',
    "–": "-",
    "...": "…",
}


def main() -> None:
    for file in sys.argv[1:]:
        path = Path(file)
        if path.suffix != ".md":
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except Exception:  # nosec B112
            continue
        new = text
        for bad, good in REPLACEMENTS.items():
            new = new.replace(bad, good)
        if new != text:
            path.write_text(new, encoding="utf-8")


if __name__ == "__main__":
    main()
