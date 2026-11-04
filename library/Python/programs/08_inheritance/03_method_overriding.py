"""Overriding methods while extending the parent implementation via super()."""


class Logger:
    def __init__(self):
        self.lines = []

    def format(self, message):
        return message

    def log(self, message):
        self.lines.append(self.format(message))
        return self


class TimestampLogger(Logger):
    def __init__(self):
        super().__init__()
        self.tick = 0

    def format(self, message):
        self.tick += 1
        return f"[t={self.tick:03d}] {super().format(message)}"


class LevelLogger(TimestampLogger):
    def __init__(self, level="INFO"):
        super().__init__()
        self.level = level

    def format(self, message):
        return super().format(f"{self.level}: {message}")

    def log(self, message, level=None):
        if level:
            self.level = level
        return super().log(message)


basic = Logger().log("plain message").log("another")
stamped = TimestampLogger().log("boot").log("ready")
leveled = LevelLogger()
leveled.log("starting").log("disk almost full", level="WARN").log("crash", level="ERROR")

for logger in (basic, stamped, leveled):
    print(f"--- {type(logger).__name__} ---")
    for line in logger.lines:
        print(line)

print("format resolution:", [cls.__name__ for cls in LevelLogger.__mro__ if "format" in vars(cls)])
