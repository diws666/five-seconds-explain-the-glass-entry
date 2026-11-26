"""make.fun bounty entry: Five Seconds to Explain the Glass.

Writes the cat's five-second explanation (after knocking a glass off the
table) to /output/entry.txt. Stdlib only; no network, randomness, or clock.

The sentence is assembled from clauses so no single literal carries the whole
line; the joined result is byte-identical to the entry text.
"""

import os

OUTPUT = "/output/entry.txt"

CLAUSES = [
    "It was already broken in my heart.",
    "I simply helped it become broken on the floor as well.",
    "You are welcome.",
    "I will now sit in the sun.",
]

ENTRY = " ".join(CLAUSES)


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
