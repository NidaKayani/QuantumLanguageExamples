"""Variadic keyword arguments with **kwargs for configuration merging."""


def make_config(**settings):
    defaults = {"debug": False, "level": 1, "name": "app"}
    return {**defaults, **settings}


def html_tag(tag, content="", **attrs):
    attr_text = "".join(f' {k.rstrip("_")}="{v}"' for k, v in attrs.items())
    return f"<{tag}{attr_text}>{content}</{tag}>"


def report(title, *items, **meta):
    lines = [f"== {title} =="]
    lines += [f"  * {item}" for item in items]
    lines += [f"  {key}: {value}" for key, value in sorted(meta.items())]
    return "\n".join(lines)


def accepts_all(*args, **kwargs):
    return len(args), sorted(kwargs)


print(make_config())
print(make_config(debug=True))
print(make_config(level=3, name="server", port=8000))

print(html_tag("p", "Hello"))
print(html_tag("a", "home", href="/index", class_="nav"))
print(html_tag("input", type="text", value="42"))

print(report("Shopping", "eggs", "milk", "bread", store="corner", budget=20))

params = {"author": "nida", "version": "1.2"}
print(report("Release", "fixes", **params))
print(accepts_all(1, 2, x=3, y=4, z=5))
