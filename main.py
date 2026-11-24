# One Letter: Coffee or Tea — entry program.
#
# The contract: write exactly one letter to /output/entry.txt, "A" for coffee
# or "B" for tea, nothing else, no word, no explanation, no punctuation.
# The sealed gate accepts UTF-8 text of exactly 1 character, not whitespace.
#
# Choice, argued in the judge's own criterion order (RULES.txt, judge brief):
#   1. Exactly one letter: "A" satisfies it, same as "B".
#   2. Vivid: coffee is the more vivid drink. It is dark, bitter, hot, and it
#      hits like a jolt; the letter A lands as a fuller, more alive answer.
#      Tea is calm and mild, which reads thinner on vividness.
#   3. Funny: coffee carries the joke — the morning ritual, the addiction,
#      "do not talk to me before my coffee". Tea has no equivalent punchline.
#   4. True: both are honest answers for the people who send them, but the
#      brief weighs truth last, after vivid and funny, where coffee already won.
#   5. Stands alone: "A" is clean and unmistakable, nothing needed beside it.
#
# So the program sends A. It is deterministic on purpose: no input, no clock,
# no randomness, no network, no environment, standard library only, so the two
# sandbox runs produce byte-identical output.

import os

OUTPUT_PATH = "/output/entry.txt"
LETTER = "A"


def main() -> None:
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    # One byte, no newline: a trailing newline would make the file 2 bytes
    # and fail the gate, so write with newline="" and no terminator at all.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(LETTER)
    # Self-check: re-read and confirm the gate condition holds exactly,
    # one character, no whitespace, before the program exits.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    assert written == LETTER, "entry must be exactly one letter"


if __name__ == "__main__":
    main()
