"""Warning Label for Humans: One Line, Big Laugh.

Writes a single-line safety warning label for every human being to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). Deterministic: the same
bytes on every run. Python standard library only.
"""

import os

LABEL = (
    "WARNING: This human will spend twenty minutes choosing what to watch, "
    "fall asleep ten minutes in, and wake up asking what happened."
)


def main() -> None:
    # The gate allows 1-160 characters; keep the label a single line.
    assert 1 <= len(LABEL) <= 160 and "\n" not in LABEL
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LABEL + "\n")


if __name__ == "__main__":
    main()
