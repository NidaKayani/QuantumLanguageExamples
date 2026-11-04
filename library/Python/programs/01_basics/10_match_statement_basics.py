"""Pattern-match commands and values with the match statement."""


def http_status(code):
    match code:
        case 200:
            return "OK"
        case 301 | 302:
            return "Redirect"
        case 404:
            return "Not Found"
        case int(c) if 500 <= c < 600:
            return "Server Error"
        case _:
            return "Unknown"


def run(command):
    match command.split():
        case ["go", direction]:
            return f"moving {direction}"
        case ["pick", "up", item]:
            return f"picked up {item}"
        case ["drop", *items] if items:
            return f"dropped {', '.join(items)}"
        case ["quit" | "exit"]:
            return "goodbye"
        case []:
            return "empty command"
        case _:
            return f"unknown: {command!r}"


def describe_point(point):
    match point:
        case (0, 0):
            return "origin"
        case (0, y):
            return f"on y-axis at {y}"
        case (x, 0):
            return f"on x-axis at {x}"
        case (x, y) if x == y:
            return f"on diagonal at {x}"
        case (x, y):
            return f"at ({x}, {y})"


for code in (200, 302, 404, 503, 999):
    print(code, "->", http_status(code))

for cmd in ("go north", "pick up lamp", "drop key coin", "exit", "", "dance wildly"):
    print(f"{cmd!r:18} -> {run(cmd)}")

for p in ((0, 0), (0, 5), (3, 0), (4, 4), (2, 7)):
    print(p, "->", describe_point(p))
