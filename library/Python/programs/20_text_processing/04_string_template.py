"""Templating with string.Template: substitute, safe_substitute, custom delimiters, and mail merge."""
from string import Template

LETTER = Template("""\
Dear $title $last_name,

Your order #$order_id of $count item(s) totalling $$${total} has shipped.
Expected delivery: ${eta}.

Regards,
$company""")


class PercentTemplate(Template):
    delimiter = "%"


class BraceOnlyTemplate(Template):
    pattern = r"""
    \{\{(?:
      (?P<escaped>\{\{) |
      \s*(?P<named>[_a-z][_a-z0-9]*)\s*\}\} |
      \s*(?P<braced>[_a-z][_a-z0-9]*)\s*\}\} |
      (?P<invalid>)
    )
    """


CUSTOMERS = [
    {"title": "Ms.", "last_name": "Rivera", "order_id": 10421, "count": 3, "total": "149.97",
     "eta": "Tuesday"},
    {"title": "Dr.", "last_name": "Okafor", "order_id": 10422, "count": 1, "total": "19.50",
     "eta": "Friday"},
]


def main():
    for customer in CUSTOMERS:
        print(LETTER.substitute(customer, company="Acme Widgets"))
        print("-" * 40)
    partial = LETTER.safe_substitute(title="Mr.", last_name="Lee")
    print("safe_substitute leaves unknown placeholders:")
    print("  " + partial.splitlines()[2])
    try:
        LETTER.substitute(title="Mr.")
    except KeyError as exc:
        print("substitute raises KeyError for missing", exc)
    print("Identifiers:", LETTER.get_identifiers())
    print("Is valid:", LETTER.is_valid())
    pct = PercentTemplate("Disk usage on %host is %{pct}%% of %total")
    print(pct.substitute(host="db01", pct=87, total="2 TB"))
    moustache = BraceOnlyTemplate("Hello {{ name }}, you have {{count}} new $messages")
    print(moustache.substitute(name="Sam", count=4))
    rows = [Template("| $sku | $qty |").substitute(sku=s, qty=q) for s, q in [("A-1", 4), ("B-22", 10)]]
    print("\n".join(rows))


if __name__ == "__main__":
    main()
