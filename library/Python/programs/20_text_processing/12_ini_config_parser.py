"""A hand-written INI parser with sections, typed values, interpolation, and error reporting."""
import re
from collections import OrderedDict

CONFIG = """\
; Application configuration
[DEFAULT]
base_dir = /srv/app
log_level = info

[server]
host = 0.0.0.0
port = 8080
workers = 4
debug = no
static = ${base_dir}/static

[database]
url = postgres://db.internal:5432/main
pool_size = 10
timeout = 2.5
# multi-line values continue with indentation
replicas = db-r1.internal
    db-r2.internal
    db-r3.internal

[logging]
log_level = debug
file = ${base_dir}/logs/app.log
"""

SECTION = re.compile(r"^\[(?P<name>[^\]]+)\]\s*$")
OPTION = re.compile(r"^(?P<key>[\w.]+)\s*[=:]\s*(?P<value>.*)$")
BOOLEANS = {"yes": True, "true": True, "on": True, "no": False, "false": False, "off": False}


class ConfigError(Exception):
    pass


def parse_ini(text):
    sections = OrderedDict(DEFAULT=OrderedDict())
    current, last_key = None, None
    for lineno, raw in enumerate(text.splitlines(), 1):
        if not raw.strip() or raw.lstrip().startswith((";", "#")):
            continue
        if raw[0] in " \t" and last_key:
            sections[current][last_key] += "\n" + raw.strip()
            continue
        if m := SECTION.match(raw):
            current = m["name"]
            sections.setdefault(current, OrderedDict())
            last_key = None
        elif (m := OPTION.match(raw)) and current:
            last_key = m["key"].lower()
            sections[current][last_key] = m["value"].strip()
        else:
            raise ConfigError(f"line {lineno}: cannot parse {raw!r}")
    return sections


def resolve(sections, section, key):
    merged = {**sections["DEFAULT"], **sections.get(section, {})}
    value = merged[key]
    value = re.sub(r"\$\{(\w+)\}", lambda m: resolve(sections, section, m[1]), value)
    return value


def typed(value):
    if value.lower() in BOOLEANS:
        return BOOLEANS[value.lower()]
    for kind in (int, float):
        try:
            return kind(value)
        except ValueError:
            pass
    return value.split("\n") if "\n" in value else value


def main():
    sections = parse_ini(CONFIG)
    for name, options in sections.items():
        if name == "DEFAULT":
            continue
        print(f"[{name}]")
        keys = list(options) + [k for k in sections["DEFAULT"] if k not in options]
        for key in keys:
            value = typed(resolve(sections, name, key))
            print(f"  {key:<10} = {value!r:<45} ({type(value).__name__})")
    try:
        parse_ini("[ok]\nthis line is wrong\n")
    except ConfigError as err:
        print("ConfigError:", err)


if __name__ == "__main__":
    main()
