"""Parse structured text with partition and rpartition."""

print("key=value".partition("="))
print("no separator".partition("="))
print("a.b.c.txt".rpartition("."))

headers = """Content-Type: text/html; charset=utf-8
Content-Length: 1024
Server: example/1.0
X-Note: contains: a colon"""

parsed = {}
for line in headers.splitlines():
    name, _, value = line.partition(":")
    parsed[name.strip().lower()] = value.strip()
for k, v in parsed.items():
    print(f"{k!r}: {v!r}")

content_type, _, params = parsed["content-type"].partition(";")
param_key, _, param_val = params.strip().partition("=")
print("type:", content_type, "| param:", param_key, "->", param_val)

emails = ["ada@example.com", "grace.hopper@navy.mil", "invalid-address", "x@y"]
for email in emails:
    user, at, domain = email.partition("@")
    if not at:
        print(f"{email}: missing @")
        continue
    host, dot, tld = domain.rpartition(".")
    print(f"{email}: user={user} host={host or '?'} tld={tld if dot else '?'}")

url = "https://example.com:8443/path/to/page?q=python&lang=en#top"
scheme, _, rest = url.partition("://")
rest, _, fragment = rest.partition("#")
rest, _, query = rest.partition("?")
hostport, _, path = rest.partition("/")
host, _, port = hostport.partition(":")
print(f"scheme={scheme} host={host} port={port} path=/{path}")
print("query:", dict(p.split("=") for p in query.split("&")), "fragment:", fragment)
