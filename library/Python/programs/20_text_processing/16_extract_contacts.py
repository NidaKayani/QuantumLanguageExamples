"""Extract and normalise emails, URLs, phone numbers, dates and hashtags from free text with re."""
import re

MESSAGE = """
Hi team -- please send the Q3 numbers to Jane.Doe@Example.com or finance-team@corp.example.org
before 2024-09-30. Backup contact: bob_smith+reports@mail.example.net (not bob@@broken).
Call +1 (555) 010-2368 or 555.010.9999, ext. 42; the London office is +44 20 7946 0958.
Dashboards: https://dash.example.com/q3?view=summary and http://intranet.local/reports/
Old link www.example.org/legacy is retired. Meeting on 03/10/2024 at 14:30. #finance #Q3Report
"""

EMAIL = re.compile(r"\b[\w.+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}\b")
URL = re.compile(r"\b(?:https?://|www\.)[^\s,;]+[^\s,;.]")
PHONE = re.compile(r"(?:\+\d{1,3}[\s-]?)?(?:\(\d{3}\)|\d{2,4})[\s.-]?\d{3,4}[\s.-]?\d{4}")
ISO_DATE = re.compile(r"\b(\d{4})-(\d{2})-(\d{2})\b")
US_DATE = re.compile(r"\b(\d{2})/(\d{2})/(\d{4})\b")
HASHTAG = re.compile(r"(?<!\w)#(\w+)")


def normalise_phone(raw):
    digits = re.sub(r"\D", "", raw)
    if raw.strip().startswith("+"):
        return "+" + digits
    return "+1" + digits if len(digits) == 10 else digits


def main():
    emails = sorted({e.lower() for e in EMAIL.findall(MESSAGE)})
    print("Emails:")
    for e in emails:
        user, domain = e.split("@")
        print(f"  {e:<40} user={user:<20} domain={domain}")
    print("URLs:")
    for u in URL.findall(MESSAGE):
        scheme = "https" if u.startswith("https") else "http"
        print(f"  {u} ({scheme})")
    print("Phones:")
    for m in PHONE.finditer(MESSAGE):
        print(f"  {m.group().strip():<20} -> {normalise_phone(m.group())}")
    dates = [f"{y}-{mo}-{d}" for y, mo, d in ISO_DATE.findall(MESSAGE)]
    dates += [f"{y}-{mo}-{d}" for mo, d, y in US_DATE.findall(MESSAGE)]
    print("Dates (ISO):", sorted(dates))
    print("Hashtags:", [t.lower() for t in HASHTAG.findall(MESSAGE)])
    redacted = EMAIL.sub(lambda m: m.group()[0] + "***@" + m.group().split("@")[1], MESSAGE)
    redacted = PHONE.sub("[phone]", redacted)
    print("Redacted first lines:")
    for line in redacted.strip().splitlines()[:3]:
        print("  " + line)


if __name__ == "__main__":
    main()
