"""Convert a small Markdown document to plain text: headings, emphasis, links, lists, code."""
import re
import textwrap

MARKDOWN = """\
# Release Notes

Version **2.4** brings *faster* builds and a new `--profile` flag.
See the [changelog](https://example.com/changes) for details.

## Highlights

- Incremental compilation is **3x** faster
- New `quantum fmt` command
  1. formats source files
  2. checks style in CI

## Example

```
quantum build --profile main.qt
```

> Note: the old `--timing` flag is deprecated.

---
Thanks to all [contributors](https://example.com/people)!
"""


def inline(text, links):
    def link(m):
        links.append(m.group(2))
        return f"{m.group(1)}[{len(links)}]"

    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, text)
    text = re.sub(r"\*\*(.+?)\*\*", lambda m: m.group(1).upper(), text)
    text = re.sub(r"\*(.+?)\*", r"_\1_", text)
    return re.sub(r"`([^`]+)`", r"'\1'", text)


def convert(md, width=60):
    out, links, in_code = [], [], False
    for line in md.splitlines():
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            out.append("    " + line)
        elif m := re.match(r"(#{1,6})\s+(.*)", line):
            title = inline(m.group(2), links)
            underline = "=" if len(m.group(1)) == 1 else "-"
            out += ["", title, underline * len(title)]
        elif m := re.match(r"(\s*)[-*]\s+(.*)", line):
            out.append(f"{m.group(1)}  o {inline(m.group(2), links)}")
        elif m := re.match(r"(\s*)(\d+)\.\s+(.*)", line):
            out.append(f"{m.group(1)}  {m.group(2)}) {inline(m.group(3), links)}")
        elif line.startswith(">"):
            out.append("  | " + inline(line.lstrip("> "), links))
        elif re.fullmatch(r"-{3,}", line):
            out.append("~" * width)
        elif line.strip():
            out.append(textwrap.fill(inline(line, links), width))
        else:
            out.append("")
    if links:
        out += ["", "Links:"] + [f"  [{i}] {url}" for i, url in enumerate(links, 1)]
    return "\n".join(out).strip("\n")


def main():
    text = convert(MARKDOWN)
    print(text)
    print()
    print(f"Input {len(MARKDOWN.splitlines())} lines -> output {len(text.splitlines())} lines")


if __name__ == "__main__":
    main()
