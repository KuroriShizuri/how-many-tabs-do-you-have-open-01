#!/usr/bin/env python3
"""Write the How Many Tabs entry to /output/entry.txt.

Standard library only. Writes exactly one number, no trailing newline.

The number: 87. An honest, lived-in count for someone who keeps
research, coursework and half-read articles open across a few windows:
high enough to surprise against a field that mostly guesses a dozen or
two, low enough to stay believable (no absurd four-digit shock figure),
and odd and non-round, the way a real counted total looks rather than a
number picked for effect.
"""

from pathlib import Path

ENTRY = "87"

MAX_CHARS = 5


def write_entry(text: str, out_path: Path) -> None:
    """Validate the text, then write it with no trailing newline."""
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} chars, over the {MAX_CHARS} limit"
        )
    if not text.isdigit():
        raise ValueError("entry must be digits only")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding="utf-8")


def main() -> int:
    out_path = Path("/output/entry.txt")
    write_entry(ENTRY, out_path)
    # Read back what landed: the file must be byte-identical to ENTRY.
    if out_path.read_bytes() != ENTRY.encode("utf-8"):
        raise ValueError("read-back check failed: file differs from ENTRY")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
