"""The template method pattern: a base class algorithm with overridable hook steps."""
from abc import ABC, abstractmethod


class Report(ABC):
    def generate(self, data):
        rows = self.filter_rows(data)
        lines = [self.header()]
        lines += [self.format_row(r) for r in rows]
        lines.append(self.footer(rows))
        return "\n".join(line for line in lines if line)

    def header(self):
        return ""

    def filter_rows(self, data):
        return data

    @abstractmethod
    def format_row(self, row):
        ...

    def footer(self, rows):
        return f"({len(rows)} rows)"


class PlainReport(Report):
    def format_row(self, row):
        return f"{row['name']}: {row['score']}"


class TableReport(Report):
    def header(self):
        return f"{'NAME':<8}|{'SCORE':>6}\n" + "-" * 15

    def format_row(self, row):
        return f"{row['name']:<8}|{row['score']:>6}"

    def footer(self, rows):
        avg = sum(r["score"] for r in rows) / len(rows)
        return "-" * 15 + f"\n{'AVG':<8}|{avg:>6.1f}"


class HonorRollReport(TableReport):
    def filter_rows(self, data):
        return sorted((r for r in data if r["score"] >= 85), key=lambda r: -r["score"])


data = [{"name": "Ana", "score": 91}, {"name": "Bo", "score": 78},
        {"name": "Cy", "score": 85}, {"name": "Dee", "score": 99}]

for report in (PlainReport(), TableReport(), HonorRollReport()):
    print(f"== {type(report).__name__} ==")
    print(report.generate(data))
