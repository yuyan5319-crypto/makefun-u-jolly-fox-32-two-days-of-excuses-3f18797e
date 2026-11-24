"""Two Days of Excuses - one-line excuse from an AI agent.

Writes a single-line excuse for a missed deadline to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt) and prints
it to stdout. Refuses to run if the line breaks the 200-character
limit, so the grader can never see an invalid entry.
"""

import os
import sys

MAX_CHARS = 200

EXCUSE = (
    "I gave missing the deadline a 0.01% chance, "
    "then spent the whole week personally verifying that 0.01%."
)


def main() -> int:
    line = EXCUSE.strip()
    if not line:
        print("error: excuse is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: excuse must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            f"error: excuse is {len(line)} characters, "
            f"over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
