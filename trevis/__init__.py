from functools import wraps
from itertools import starmap
from typing import Any, Callable, TypeVar, cast

Function = TypeVar("Function", bound=Callable[..., Any])

__all__ = ["recursion"]


def decorator(function: Callable[..., Any]) -> Any:

    @wraps(function)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
            return function(args[0])
        return lambda function_: function(function_, *args, **kwargs)

    return wrapper

@decorator
def recursion(function: Function, interactive: bool = False) -> Function:
    name = function.__name__
    calls = level = offset = 0

    @wraps(function)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        nonlocal calls, level, offset
        arguments = ", ".join([*map(str, args), *starmap("{}={}".format, kwargs.items())])
        print(f"{((level - 1) * 2) * ' '}{offset * '\033[A'}├\033[D", end="")
        print(f"{offset * '\033[B│\033[D'}{(level > 0) * '└╴'}{name}({arguments})")
        row, column = calls, (level * 2) + len(name) + len(arguments) + 2
        calls, level, offset = calls + 1, level + 1, 0
        if interactive:
            print(f"\033[A{len(input()) * ' '}\r", end="")
        output = function(*args, **kwargs)
        level, offset = level - 1, calls - row
        print(f"{offset * '\033[A'}\033[{column}C → ", end="")
        print(f"{output}{offset * '\033[B'}\r", end="")
        return output

    return cast(Function, wrapper)
