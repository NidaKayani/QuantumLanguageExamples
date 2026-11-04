"""Abstract properties and classmethods in an ABC for a plugin-style hierarchy."""
from abc import ABC, abstractmethod


class Exporter(ABC):
    @property
    @abstractmethod
    def extension(self):
        """File extension produced by this exporter."""

    @classmethod
    @abstractmethod
    def supports(cls, data):
        ...

    @abstractmethod
    def export(self, rows):
        ...

    def filename(self, stem):
        return f"{stem}.{self.extension}"


class CsvExporter(Exporter):
    extension = "csv"

    @classmethod
    def supports(cls, data):
        return all(isinstance(r, (list, tuple)) for r in data)

    def export(self, rows):
        return "\n".join(",".join(map(str, r)) for r in rows)


class JsonLinesExporter(Exporter):
    @property
    def extension(self):
        return "jsonl"

    @classmethod
    def supports(cls, data):
        return all(isinstance(r, dict) for r in data)

    def export(self, rows):
        import json
        return "\n".join(json.dumps(r, sort_keys=True) for r in rows)


def pick_exporter(data):
    for cls in Exporter.__subclasses__():
        if cls.supports(data):
            return cls()
    raise LookupError("no exporter supports this data")


datasets = {
    "points": [(1, 2), (3, 4), (5, 6)],
    "people": [{"name": "Ana", "age": 31}, {"name": "Raj", "age": 27}],
    "mixed": [(1, 2), {"x": 1}],
}
for name, data in datasets.items():
    try:
        exporter = pick_exporter(data)
    except LookupError as exc:
        print(f"{name}: {exc}")
        continue
    print(f"{exporter.filename(name)} via {type(exporter).__name__}:")
    print(exporter.export(data))
print("registered exporters:", [c.__name__ for c in Exporter.__subclasses__()])
