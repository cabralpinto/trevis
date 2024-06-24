# Trevis

Easily visualize recursive functions in the console.

```python
from trevis import recursion

@recursion
def fib(n: int) -> int:
    if n < 2: return n
    return fib(n - 1) + fib(n - 2)

fib(4)
```
```python
# output
fib(4) → 3
├╴fib(3) → 2
│ ├╴fib(2) → 1
│ │ ├╴fib(1) → 1
│ │ └╴fib(0) → 0
│ └╴fib(1) → 1
└╴fib(2) → 1
  ├╴fib(1) → 1
  └╴fib(0) → 0
```
## Features

- 🕹️ **Interactive mode**: Review each function execution interactively, advancing to the next step by pressing Enter. This mode enhances comprehension and debugging by providing a clear visual representation of each step. Enable with `recursion(interactive=True)`.
- 🌈 **Syntax highlighting (*upcoming*)**: Enable syntax highlighting in the tree for improved readability. Coming in a future version.
- 🎲 **Non-deterministic function visualization (*upcoming*)**: Visualize of all possible execution paths for non-deterministic functions. Coming in a future version.

## Installation

Ensure you have Python 3.6 or higher, then install Trevis using pip:

```bash
pip install trevis
```

## Contribution

Contributions are welcome! Feel free to submit an [issue](https://github.com/cabralpinto/trevis/issues) or [pull request](https://github.com/cabralpinto/trevis/pulls).

## License

Trevis is licensed under the [MIT License](LICENSE).
