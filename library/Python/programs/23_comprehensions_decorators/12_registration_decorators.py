"""Registration decorators building a command dispatcher and a plugin registry."""

COMMANDS = {}


def command(name, *aliases, help=""):
    def register(func):
        for key in (name, *aliases):
            if key in COMMANDS:
                raise KeyError(f"duplicate command {key!r}")
            COMMANDS[key] = func
        func.help = help
        func.command_name = name
        return func
    return register


stack = []


@command("push", "p", help="push numbers onto the stack")
def push(*args):
    stack.extend(float(a) for a in args)
    return stack


@command("add", "+", help="add the top two values")
def add():
    stack.append(stack.pop() + stack.pop())
    return stack


@command("mul", "*", help="multiply the top two values")
def mul():
    stack.append(stack.pop() * stack.pop())
    return stack


@command("clear", help="empty the stack")
def clear():
    stack.clear()
    return stack


def dispatch(line):
    name, *args = line.split()
    handler = COMMANDS.get(name)
    if handler is None:
        return f"unknown command {name!r}"
    return handler(*args)


for line in ["push 3 4", "+", "p 5", "mul", "push 2", "*", "pop", "clear"]:
    print(f"> {line:<10} {dispatch(line)}")

print("Help:")
for func in sorted({f for f in COMMANDS.values()}, key=lambda f: f.command_name):
    aliases = sorted(k for k, v in COMMANDS.items() if v is func and k != func.command_name)
    print(f"  {func.command_name:<6} {str(aliases):<8} {func.help}")


class Plugin:
    registry = []

    @classmethod
    def register(cls, priority=0):
        def decorator(plugin_cls):
            cls.registry.append((priority, plugin_cls))
            cls.registry.sort(key=lambda item: -item[0])
            return plugin_cls
        return decorator


@Plugin.register(priority=5)
class Spellcheck:
    def run(self, text):
        return text.replace("teh", "the")


@Plugin.register(priority=10)
class Trim:
    def run(self, text):
        return " ".join(text.split())


@Plugin.register()
class Shout:
    def run(self, text):
        return text.upper()


text = "  teh   quick  brown fox  "
for priority, plugin in Plugin.registry:
    text = plugin().run(text)
    print(f"after {plugin.__name__:<10} (priority {priority:>2}): {text!r}")
