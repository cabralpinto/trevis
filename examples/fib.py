from trevis import recursion

@recursion(interactive=True)
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

fib(5)
