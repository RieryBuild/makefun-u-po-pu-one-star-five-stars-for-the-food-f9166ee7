"""One-star alien-tourist review of Earth, with a real compliment for the fries.

The entry is one sentence (142 chars). It is built from its two halves so the
complaint and the turn stay visible as separate pieces: the grievance first,
then the food compliment that undercuts it.
"""

import os

GRIEVANCE = "I molted in public and got fined for littering my own skin, so one star"
TURN = "though the fries were so good I would molt twice for another handful"

LINE = GRIEVANCE + ", " + TURN + "."


def validate(line):
    assert line.strip(), "entry must not be whitespace-only"
    assert 1 <= len(line) <= 200, "entry must be 1-200 chars"
    assert line.count(".") == 1 and line.endswith("."), "entry must be one sentence"
    assert "\n" not in line, "entry must be a single line"
    assert "one star" in line.lower(), "entry must state the one-star rating"
    return line


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(validate(LINE))


if __name__ == "__main__":
    main()
