"""Letter-frequency histograms: horizontal and vertical bar charts plus a pangram checker."""
from collections import Counter
from string import ascii_lowercase

PASSAGE = """Pack my box with five dozen liquor jugs. The five boxing wizards jump quickly.
Sphinx of black quartz, judge my vow. How vexingly quick daft zebras jump!
Text processing is mostly about counting things and then presenting them clearly."""


def letter_counts(text):
    return Counter(ch for ch in text.lower() if ch in ascii_lowercase)


def horizontal(counts, width=40):
    peak = max(counts.values())
    lines = []
    for letter in ascii_lowercase:
        n = counts.get(letter, 0)
        bar = "#" * round(n / peak * width)
        lines.append(f"{letter} {n:>3} {bar}")
    return lines


def vertical(counts, height=8):
    peak = max(counts.values())
    scaled = {ch: round(counts.get(ch, 0) / peak * height) for ch in ascii_lowercase}
    rows = []
    for level in range(height, 0, -1):
        rows.append("".join("#" if scaled[ch] >= level else " " for ch in ascii_lowercase))
    rows.append(ascii_lowercase)
    return rows


def missing_letters(sentence):
    return sorted(set(ascii_lowercase) - set(sentence.lower()))


def main():
    counts = letter_counts(PASSAGE)
    total = sum(counts.values())
    print(f"{total} letters, {len(counts)} distinct")
    print("\n".join(horizontal(counts)))
    print()
    print("\n".join(vertical(counts)))
    print()
    vowels = sum(counts[v] for v in "aeiou")
    print(f"Vowels {vowels} ({vowels / total:.1%}), consonants {total - vowels}")
    order = "".join(ch for ch, _ in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])))
    print("Frequency order:", order)
    for sentence in PASSAGE.replace("!", ".").split(".")[:5]:
        sentence = sentence.strip()
        if sentence:
            gaps = missing_letters(sentence)
            verdict = "pangram" if not gaps else f"missing {''.join(gaps)}"
            print(f"  {sentence[:45]:<45} {verdict}")


if __name__ == "__main__":
    main()
