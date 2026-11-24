"""Real-Life Patch Notes: The Comedy Changelog.

Writes one patch note to /output/entry.txt (or $OUTPUT_DIR/entry.txt).
"""

import os

PATCH_NOTE = (
    "v2.3.1: fixed a bug where crossing a doorway deleted the reason "
    "you entered the room; no undo, no autosave, no log."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(PATCH_NOTE + "\n")


if __name__ == "__main__":
    main()
