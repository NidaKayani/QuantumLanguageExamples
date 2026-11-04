"""A custom sequence (a playlist) implementing __len__, __getitem__ with slices, __contains__ and more."""


class Playlist:
    def __init__(self, name, tracks=()):
        self.name = name
        self._tracks = list(tracks)

    def __len__(self):
        return len(self._tracks)

    def __getitem__(self, index):
        if isinstance(index, slice):
            return Playlist(f"{self.name}[{index.start}:{index.stop}:{index.step}]", self._tracks[index])
        if isinstance(index, str):
            for track in self._tracks:
                if track[0].lower() == index.lower():
                    return track
            raise KeyError(index)
        return self._tracks[index]

    def __setitem__(self, index, value):
        self._tracks[index] = value

    def __delitem__(self, index):
        del self._tracks[index]

    def __contains__(self, title):
        return any(t[0].lower() == title.lower() for t in self._tracks)

    def __iter__(self):
        return iter(self._tracks)

    def __reversed__(self):
        return reversed(self._tracks)

    def __add__(self, other):
        return Playlist(f"{self.name}+{other.name}", self._tracks + other._tracks)

    def __bool__(self):
        return bool(self._tracks)

    def __repr__(self):
        return f"Playlist({self.name!r}, {len(self)} tracks)"

    @property
    def duration(self):
        seconds = sum(t[1] for t in self._tracks)
        return f"{seconds // 60}:{seconds % 60:02d}"


mix = Playlist("mix", [("Intro", 95), ("Blue", 214), ("Neon", 187), ("Drift", 243), ("Outro", 120)])
print(mix, "duration", mix.duration)
print("first:", mix[0], "| last:", mix[-1], "| by title:", mix["neon"])
print("slice:", mix[1:4], [t[0] for t in mix[1:4]])
print("every other:", [t[0] for t in mix[::2]])
print("contains 'blue'?", "blue" in mix, "| contains 'Red'?", "Red" in mix)
print("reversed:", [t[0] for t in reversed(mix)])
print("sorted by length:", [t[0] for t in sorted(mix, key=lambda t: t[1])])

mix[1] = ("Blue (remix)", 260)
del mix[0]
print("after edits:", [t[0] for t in mix], mix.duration)

extra = Playlist("extra", [("Coda", 60)])
combined = mix + extra
print(combined, combined.duration)
print("empty is falsy:", not Playlist("empty"), "| enumerate:", list(enumerate(t[0] for t in extra)))
try:
    mix["missing"]
except KeyError as exc:
    print("KeyError:", exc)
total = 0
for title, seconds in mix:
    total += seconds
print("iterated total seconds:", total, "| index of Drift:", [t[0] for t in mix].index("Drift"))
