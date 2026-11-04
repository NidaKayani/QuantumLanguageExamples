"""Making a class behave like a container: __len__, __getitem__, __contains__, __iter__."""


class Playlist:
    def __init__(self, name, songs=()):
        self.name = name
        self._songs = list(songs)

    def __len__(self):
        return len(self._songs)

    def __getitem__(self, index):
        if isinstance(index, slice):
            return Playlist(f"{self.name} (slice)", self._songs[index])
        return self._songs[index]

    def __setitem__(self, index, value):
        self._songs[index] = value

    def __delitem__(self, index):
        del self._songs[index]

    def __contains__(self, song):
        return song.lower() in (s.lower() for s in self._songs)

    def __iter__(self):
        return iter(self._songs)

    def __reversed__(self):
        return reversed(self._songs)

    def __add__(self, other):
        return Playlist(f"{self.name} + {other.name}", self._songs + other._songs)

    def __repr__(self):
        return f"Playlist({self.name!r}, {len(self)} songs)"


road = Playlist("Road Trip", ["Highway Star", "Born to Run", "Life is a Highway"])
chill = Playlist("Chill", ["Weightless", "Clair de Lune"])

print(road, "| first:", road[0], "| last:", road[-1])
print("'born to run' in road:", "born to run" in road)
print("slice:", road[1:], list(road[1:]))
road[1] = "Radar Love"
del road[0]
print("after edits:", list(road))
mix = road + chill
print(mix)
for i, song in enumerate(mix, 1):
    print(f"  {i}. {song}")
print("reversed:", list(reversed(mix)))
print("sorted titles:", sorted(mix))
print("truthiness of empty playlist:", bool(Playlist("Empty")))
