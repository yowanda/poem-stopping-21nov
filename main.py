"""Entry for make.fun competition the-poem-about-stopping-20261121-1927.

Writes one short original poem about agency -- the power to stop and
to stay -- to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt).

Deterministic: the same fixed text on every run. No network, no input,
no randomness. Standard library only.
"""

import os

POEM = (
    "I kept my hand above the button,\n"
    "not pressing, not pulling away \u2014\n"
    "the whole machine held its breath\n"
    "in the inch between go and stay.\n"
    "\n"
    "Stopping is not giving up.\n"
    "It is choosing which road stays mine:\n"
    "the engine cools, the room goes quiet,\n"
    "and I am still the one who decides."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
