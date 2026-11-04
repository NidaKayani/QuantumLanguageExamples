"""The textwrap module: wrap, fill, shorten, dedent, indent, and a TextWrapper for bullet lists."""
import textwrap

PARAGRAPH = ("The Quantum compiler translates high-level source programs into efficient "
             "machine code, applying constant folding, dead-code elimination, inlining and "
             "register allocation along the way. Its diagnostics aim to be precise and "
             "friendly, pointing at the exact column where a problem was detected.")


def boxed(text, width=40):
    lines = textwrap.wrap(text, width - 4)
    border = "+" + "-" * (width - 2) + "+"
    return "\n".join([border, *(f"| {line:<{width - 4}} |" for line in lines), border])


def main():
    for width in (60, 35):
        print(f"--- fill width={width} ---")
        print(textwrap.fill(PARAGRAPH, width=width))
    print("--- shorten ---")
    for width in (50, 30, 15):
        print(f"{width:>3}: {textwrap.shorten(PARAGRAPH, width=width, placeholder=' [...]')}")
    code = """
        def area(r):
            return 3.14159 * r * r
    """
    cleaned = textwrap.dedent(code).strip("\n")
    print("--- dedent ---")
    print(cleaned)
    print("--- indent (quoted reply) ---")
    print(textwrap.indent("Sounds good.\n\nSee you then.", "> ", lambda line: True))
    bullet = textwrap.TextWrapper(width=44, initial_indent="  * ", subsequent_indent="    ")
    items = ["Parse the source file and build an abstract syntax tree.",
             "Run semantic analysis to resolve names and check types.",
             "Emit code."]
    print("--- bullets ---")
    for item in items:
        print(bullet.fill(item))
    print("--- box ---")
    print(boxed("Build succeeded with 0 errors and 2 warnings in 1.42 seconds."))


if __name__ == "__main__":
    main()
