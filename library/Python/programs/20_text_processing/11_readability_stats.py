"""Sentence splitting, heuristic syllable counting, and Flesch readability scores."""
import re
from dataclasses import dataclass
from statistics import mean, pstdev

SAMPLES = {
    "children": "The cat sat on the mat. It was a fat cat. The dog ran to the cat. "
                "They played all day. Then they went to sleep.",
    "news": "Officials announced on Tuesday that the municipal transportation authority "
            "will expand weekend service. The decision follows months of public consultation. "
            "Critics argue the additional funding should prioritise infrastructure maintenance.",
    "academic": "Notwithstanding considerable methodological heterogeneity, the systematic "
                "evaluation demonstrated statistically significant improvements. Consequently, "
                "practitioners should incorporate these interdisciplinary recommendations judiciously.",
}


def split_sentences(text):
    return [s for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s]


def syllables(word):
    word = word.lower()
    groups = re.findall(r"[aeiouy]+", word)
    count = len(groups)
    if word.endswith("e") and not word.endswith(("le", "ee")) and count > 1:
        count -= 1
    return max(count, 1)


@dataclass
class Stats:
    sentences: int
    words: int
    syllables: int
    sentence_lengths: list

    @property
    def flesch_ease(self):
        return 206.835 - 1.015 * self.words / self.sentences - 84.6 * self.syllables / self.words

    @property
    def grade(self):
        return 0.39 * self.words / self.sentences + 11.8 * self.syllables / self.words - 15.59


def analyse(text):
    sentences = split_sentences(text)
    words = re.findall(r"[A-Za-z']+", text)
    return Stats(len(sentences), len(words), sum(map(syllables, words)),
                 [len(re.findall(r"[A-Za-z']+", s)) for s in sentences])


def label(score):
    for limit, name in ((90, "very easy"), (70, "easy"), (50, "standard"), (30, "difficult")):
        if score >= limit:
            return name
    return "very confusing"


def main():
    print("Syllables:", {w: syllables(w) for w in
                         ["cat", "table", "simple", "recommendation", "make", "agree", "rhythm"]})
    print(f"{'sample':<10}{'sent':>5}{'words':>6}{'syl':>5}{'ease':>8}{'grade':>7}  verdict")
    for name, text in SAMPLES.items():
        s = analyse(text)
        print(f"{name:<10}{s.sentences:>5}{s.words:>6}{s.syllables:>5}"
              f"{s.flesch_ease:>8.1f}{s.grade:>7.1f}  {label(s.flesch_ease)}")
    s = analyse(SAMPLES["children"])
    print(f"Children's sentence lengths {s.sentence_lengths}: mean {mean(s.sentence_lengths):.2f}, "
          f"stdev {pstdev(s.sentence_lengths):.2f}")
    print("Split check:", split_sentences("Dr. Smith arrived. Was he late? No! He was early."))


if __name__ == "__main__":
    main()
