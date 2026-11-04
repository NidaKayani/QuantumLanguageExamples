"""Functions as first-class objects: attributes, registries, and dispatch tables."""

COMMANDS = {}


def command(name, help_text=""):
    def register(func):
        func.command_name = name
        func.help_text = help_text
        COMMANDS[name] = func
        return func
    return register


@command("add", "Add numbers together")
def cmd_add(*nums):
    return sum(nums)


@command("max", "Largest number")
def cmd_max(*nums):
    return max(nums)


@command("avg", "Arithmetic mean")
def cmd_avg(*nums):
    return sum(nums) / len(nums)


def run(line):
    name, *args = line.split()
    func = COMMANDS.get(name)
    if func is None:
        return f"unknown command {name!r}"
    return f"{name} -> {func(*map(float, args))}"


def counter():
    counter.calls += 1
    return counter.calls


counter.calls = 0

print("Available commands:")
for name, func in sorted(COMMANDS.items()):
    print(f"  {name:<4} {func.help_text}")

for line in ["add 1 2 3", "max 4 9 2", "avg 2 4 6 8", "mul 2 3"]:
    print(run(line))

for _ in range(3):
    counter()
print("counter.calls =", counter.calls)
print("callable checks:", callable(cmd_add), callable(42))
print("function name:", cmd_avg.__name__, "| registered as:", cmd_avg.command_name)
print("same object in registry:", COMMANDS["max"] is cmd_max)
