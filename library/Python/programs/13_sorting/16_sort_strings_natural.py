"""Natural ("human") sort order for strings containing numbers."""

import re


def natural_key(s: str):
    return [int(part) if part.isdigit() else part.lower() for part in re.split(r"(\d+)", s)]


files = ["file10.txt", "file2.txt", "File1.txt", "file1b.txt", "file20.txt", "file3.txt", "readme", "file02.txt"]
print("lexicographic:", sorted(files))
print("natural:      ", sorted(files, key=natural_key))

chapters = ["Chapter 10", "Chapter 9", "Chapter 1", "Appendix B", "Appendix A", "Chapter 2"]
print("chapters:", sorted(chapters, key=natural_key))

ips = ["10.0.0.12", "10.0.0.2", "192.168.1.1", "10.0.1.1", "9.255.255.255"]
print("IPs as strings:", sorted(ips))
print("IPs numerically:", sorted(ips, key=lambda ip: tuple(map(int, ip.split(".")))))

sizes = ["1.5 GB", "512 MB", "20 KB", "3 GB", "900 KB", "1 TB"]
UNITS = {"KB": 1, "MB": 1024, "GB": 1024 ** 2, "TB": 1024 ** 3}
def size_key(s):
    number, unit = s.split()
    return float(number) * UNITS[unit]
print("sizes:", sorted(sizes, key=size_key))

names = ["mcdonald", "MacArthur", "Mabel", "mackenzie", "McAdams"]
print("casefold sort:", sorted(names, key=str.casefold))
