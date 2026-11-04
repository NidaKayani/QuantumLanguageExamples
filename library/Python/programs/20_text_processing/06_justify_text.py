"""Left, right, centre and full justification of paragraphs, with str.ljust/rjust/center."""
from enum import Enum, auto

TEXT = ("This is an example of text justification. Each line is padded with extra spaces "
        "so that both margins line up exactly, except for the final line of the paragraph "
        "which stays left aligned as typographers expect.")


class Align(Enum):
    LEFT = auto()
    RIGHT = auto()
    CENTER = auto()
    FULL = auto()


def greedy_lines(words, width):
    lines, current = [], []
    for word in words:
        if current and len(" ".join(current + [word])) > width:
            lines.append(current)
            current = []
        current.append(word)
    if current:
        lines.append(current)
    return lines


def justify_line(words, width):
    if len(words) == 1:
        return words[0].ljust(width)
    gaps = len(words) - 1
    spaces = width - sum(map(len, words))
    base, extra = divmod(spaces, gaps)
    out = []
    for i, word in enumerate(words[:-1]):
        out.append(word + " " * (base + (1 if i < extra else 0)))
    out.append(words[-1])
    return "".join(out)


def format_paragraph(text, width, align):
    lines = greedy_lines(text.split(), width)
    result = []
    for i, words in enumerate(lines):
        line = " ".join(words)
        if align is Align.LEFT:
            result.append(line.ljust(width))
        elif align is Align.RIGHT:
            result.append(line.rjust(width))
        elif align is Align.CENTER:
            result.append(line.center(width))
        else:
            last = i == len(lines) - 1
            result.append(line.ljust(width) if last else justify_line(words, width))
    return result


def main():
    width = 36
    for align in Align:
        print(f"{align.name:-^{width + 2}}")
        for line in format_paragraph(TEXT, width, align):
            print(f"|{line}|")
    print(f"{'columns':-^{width + 2}}")
    left = format_paragraph(TEXT, 22, Align.FULL)
    right = format_paragraph(TEXT.upper(), 22, Align.CENTER)
    for a, b in zip(left, right):
        print(f"{a}  |  {b}")


if __name__ == "__main__":
    main()
