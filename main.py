"""The One-Line Exit — prints the resignation letter from entry.txt."""

import pathlib


def load_letter(path):
    text = pathlib.Path(path).read_text(encoding="utf-8")
    letter = text.strip()
    if "\n" in letter:
        raise ValueError("the exit letter must be exactly one line")
    return letter


def main():
    letter = load_letter(pathlib.Path(__file__).with_name("entry.txt"))
    print(letter)


if __name__ == "__main__":
    main()
