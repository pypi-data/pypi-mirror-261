import rich
__version__ = "0.3.2"


def hello(name):
    return f"Hello, {name}!"


def goodbye(name):
    return f"Goodbye, {name}!"


def print_bluehello(name):
    rich.print(f"Hello, [blue]{name}[/blue]! (in blue)")
