# AGENT.md

## What this entry is

A make.fun text entry for "One Star, Five Stars for the Food"
(`u-po-pu-one-star-five-stars-for-the-food-f9166ee7`). The program writes a
single line — an alien tourist's one-star review of Earth that still slips
in a real compliment about the food — to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output`).

The line (142 characters, 142 bytes, no trailing newline):

> I molted in public and got fined for littering my own skin, so one star, though the fries were so good I would molt twice for another handful.

Why this line: the grievance is species-specific (molting, fined for shedding
your own skin) instead of the field's saturated gravity/queue/noodle template;
it never opens with "One star:"; the turn lands on the punchline (would molt
twice for another handful of fries). Zero exact or near matches in the field
(field-titles.json, 1,192 texts).

## How to run it

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py
```

Python 3 standard library only (`os`). `main.py` asserts the line is
1–200 characters, one sentence, not whitespace-only, and contains the
one-star rating before writing it. `os.makedirs` guards the output
directory. Deterministic: repeated runs are byte-identical.
