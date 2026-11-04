"""Walking a class hierarchy with __subclasses__, __bases__, and __init_subclass__."""


class Plugin:
    registry = {}

    def __init_subclass__(cls, name=None, **kwargs):
        super().__init_subclass__(**kwargs)
        key = name or cls.__name__.lower()
        Plugin.registry[key] = cls
        cls.plugin_name = key


class Formatter(Plugin):
    def run(self, text):
        return text


class Upper(Formatter, name="upper"):
    def run(self, text):
        return text.upper()


class Reverse(Formatter, name="rev"):
    def run(self, text):
        return text[::-1]


class Shout(Upper, name="shout"):
    def run(self, text):
        return super().run(text) + "!!!"


class Checker(Plugin):
    pass


def tree(cls, indent=0):
    print("  " * indent + cls.__name__)
    for sub in cls.__subclasses__():
        tree(sub, indent + 1)


tree(Plugin)
print("registry:", sorted(Plugin.registry))
for key in ["upper", "rev", "shout", "formatter"]:
    plugin = Plugin.registry[key]()
    print(f"{key:<9} -> {plugin.run('Quantum')}")
print("Shout bases:", [b.__name__ for b in Shout.__bases__])
print("plugin names:", [cls.plugin_name for cls in Formatter.__subclasses__()])
