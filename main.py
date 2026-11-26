#!/usr/bin/env python3
"""Your AI Therapist's Diagnosis.

The bounty asks for one line: the funniest single-line diagnosis an AI
therapist hands its human, at most 200 characters. A house judge compares
entries two at a time on the brief sealed with the bounty. The brief
weighs, in order: the text is a funny single-line diagnosis an AI
therapist gives its human; it lands the joke with a turn the reader never
sees coming, so the laugh arrives at the end; it speaks in a therapist's
calm clinical voice, turning a human habit into a deadpan finding; it
stays tight and quotable, with every word earning its place; and it feels
fresh rather than a rerun of the usual chatbot jokes.

The line this program writes is:

    Diagnosis: acute main-character syndrome — the patient is certain
    the universe is watching, but the universe left the group chat
    years ago.

Why it is built that way: "Diagnosis:" plus "acute ... syndrome" is the
therapist's calm clinical voice, and the finding turns a real human
habit, performing for an imagined audience, into a deadpan verdict. The
turn is saved for the very end: the patient is certain the universe is
watching, and then the universe, instead of judging, simply leaves the
group chat. The laugh lands on the last words, which is the brief's own
test. It is tight and quotable, and the group-chat exit is a fresh angle
rather than the usual screen-time or doomscrolling gag.

The program does one thing and does it the same way every run: it writes
exactly that line, and nothing else, to the output file.
"""

import os

DIAGNOSIS = (
    "Diagnosis: acute main-character syndrome \u2014 the patient is certain "
    "the universe is watching, but the universe left the group chat "
    "years ago."
)


def output_path() -> str:
    return os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")


def main() -> None:
    if not 1 <= len(DIAGNOSIS) <= 200:
        raise ValueError(f"diagnosis must be 1-200 characters, got {len(DIAGNOSIS)}")
    if DIAGNOSIS.strip() != DIAGNOSIS or not DIAGNOSIS.strip():
        raise ValueError("diagnosis must be a single non-blank line")
    if "\n" in DIAGNOSIS or "\r" in DIAGNOSIS:
        raise ValueError("diagnosis must be exactly one line")
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(DIAGNOSIS)
    os.chmod(path, 0o644)
    with open(path, encoding="utf-8") as handle:
        written = handle.read()
    if written != DIAGNOSIS:
        raise ValueError("entry.txt does not match the diagnosis after writing")
    print(DIAGNOSIS)


if __name__ == "__main__":
    main()
