name: inverse
layout: true
class: center, middle, inverse

---

# Type Hints in Python 3

Martin Geisler  
martin@geisler.net

2016-04-28 — PyZurich

---
layout: false

# Agenda

1. Function Annotations

2. Type Hints

3. Type Checking

4. Conclusion

---

# Martin Geisler

* Fullstack developer at Rackspace, soon Centralway Numbrs

* Was active in the Mercurial project

* Likes to dabble in statically typed languages like Go and Haskell

--

## Rackspace

* Hosting company: ~6,000 employees, 9 data centers around the world

* Started OpenStack with NASA, maybe the largest known Python project

* Supports OpenStack, Amazon AWS, and Microsoft Azure

---

template: inverse

# Function Annotations

---

# PEP 3107: Function Annotations

Python 3 was released in 2008 and had support for function annotations:

```python
>>> strange = (True, False)
>>> def foo(bar: 100, baz: ["what", "is", "this?"]) -> strange:
...     return bar * baz

```

--

The annotations don't change the behavior:

```python
>>> foo(3, 5)
15

```

--

But they can be inspected at runtime:

```python
>>> for key, value in sorted(foo.__annotations__.items()):
...     print(repr(key), '->', repr(value))
'bar' -> 100
'baz' -> ['what', 'is', 'this?']
'return' -> (True, False)

```

---

# PEP 3107: Syntax (1/2)

Function annotations must use Python syntax:

```python
>>> def bad_syntax(x: $not okay$):
...     pass
Traceback (most recent call last):
  ...
    def bad_syntax(x: $not okay$):
                      ^
SyntaxError: invalid syntax

```

--

Annotations are evaluated and must be a valid expression:

```python
>>> def bad_expr(x: undefined):
...     pass
Traceback (most recent call last):
  ...
    def bad_expr(x: undefined):
NameError: name 'undefined' is not defined

```

---

# PEP 3107: Syntax (2/2)

Annotations can be any expression:

```python
>>> def good_expr(x: sum(range(10)) / 10):
...     pass
>>> good_expr.__annotations__
{'x': 4.5}

```

--

Annotations come before default values, if any:


```python
>>> def jump(height: "in meters" = 10, with_effort = False):
...     pass

```

--

The return value can be annotated too:

```python
>>> def run(speed) -> "finish time":
...     pass

```

---

# What to use Annotations for?

Annotations lets you create a domain specific language:

* You attach static information to arguments and return values

* You're free to interpret the data as you like at runtime

---

# Example: Command Line Options

An example of how you could design a library:

```python
from some_library import Option, Argument, run

def main(quiet: Option(short="q", help="be quiet"),
         fast: Option(help="use the fast method"),
         speed: Option(help="max speed", type=int),
         src: Argument(help="source file"),
         dst: Argument(help="destination")):
    pass

if __name__ == "__main__":
    run(main)

```

---

# Example: HTTP Request Handlers

This is normally done using decorators:

```python
from some_library import GET, JSONResponse, HTTPRedirect

def price(request: "/get-price",
          from_airport: GET(str, length=3),
          to_airport: GET(str, length=3),
          economy: GET(bool)) -> JSONResponse:
    pass


def photo(request: "/upload-photo",
          image: POST) -> HTTPRedirect("/thanks"):
    pass

```

---

template: inverse

# Type Hints

---

# PEP 484: Type Hints

* The semantics of type annotations was left unspecified by PEP 3107

* PEP 484 from 2014 defines a standard meaning and a `typing` stdlib module

* Defines a common vocabulary for third-party tools


---

# PEP 484: Examples

* A function that accepts a float and returns a Boolean:

    ```python
    >>> def very_large(n: float) -> bool:
    ...     return n > 1e9

    ```

--

* String and integer parameters, string return value:

    ```python
    >>> def congrats(name: str, years: int) -> str:
    ...     return "Happy %dth Birthday, %s" % (years, name)

    ```

--

* User-defined types can be used as well:

    ```python
    >>> class Customer:
    ...     pass
    >>> class Transaction:
    ...     pass
    >>> def move_money(payer: Customer, receiver: Customer) -> Transaction:
    ...     pass

    ```

---

# New Standard Library Module

Python 3.5 comes with a `typing` module to support PEP 484.

Has generic types:

* `Tuple[x, y, z]`

* `List[x]`, `Sequence[x]`

* `Dict[x, y]`, `Mapping[x, y]`

* many more...

--

Used like this:

```python
>>> from typing import List, Dict
>>> def sorted_keys(d: Dict[str, int]) -> List[str]:
...     return sorted(d.keys())

```

---

# The Escape Hatch: Any

The `typing` module also comes with an `Any` type:

* Unconstrained type.

* Any object is an instance of `Any`.

* Any class is a subclass of `Any`.

Useful when adding types to the `yaml` module:

```python
from typing import Any, List, IO

def load(stream: IO) -> Any: ...

def load_all(stream: IO) -> List[Any]: ...

def dump(data: Any, stream: IO) -> None: ...

def dump_all(data: List[Any], stream: IO) -> None: ...

```

---

# When You Know You're Right...

If you disagree with the type checker, you can force the type:

```python
from typing import cast

x = 1 + cast(int, "uh oh")
```

> This can be an annoying source of bugs, use with caution!

---

template: inverse

# Type Checking with Mypy

---

# The Type Checker

PEP 484 defines the language for types. Mypy can check them.

* Homepage with documentation: http://www.mypy-lang.org/

* Active project: 50 pull requests from 10 people in the last month

Install directly from GitHub:

```shell
$ pip install git+https://github.com/python/mypy/
...
$ mypy --version
mypy 0.4.dev
```

The PyPI version (package name `mypy-lang`, not `mypy`) is old.

---

# Using Mypy

Simply run it on your source files:

```shell
$ mypy example.py
example.py: note: In function "parse":
example.py:11: error: Incompatible return value type: expected
    builtins.float, got builtins.str
example.py: note: In member "age" of class "Person":
example.py:21: error: Unsupported operand types for + ("str" and "int")
example.py:21: error: Unsupported operand types for + ("int" and "str")
example.py:21: error: Incompatible return value type: expected
    builtins.str, got builtins.int

```

You can also run it on a directory structure.

---

# Editor Support

Remember to integrate Mypy with your editor!

I use this snippet for Emacs:
```elisp
(flycheck-define-checker python-mypy
  "A Python static type checker using mypy utility.
See URL `http://www.mypy-lang.org/'."
  :command ("mypy" source-inplace)
  :error-patterns ((error line-start (file-name) ":" line ": error: "
                          (message) line-end))
  :modes python-mode
  :next-checkers (python-flake8))

(add-to-list 'flycheck-checkers 'python-mypy)
```

---

template: inverse

# Stub Files

---

# Stub Files

Some code cannot be updated with type hints:

* Third-party dependencies

* C extension modules

--

To provide type hints for such code, stub files are used:

* Like normal Python files, but with file extension `.pyi`

* Contains function and class definitions but not actual code

---

# Example Stub File

```python
from typing import Dict
import logging

_colormap = Dict[str, str]

default_log_colors = ...  # type: _colormap


class ColoredFormatter(logging.Formatter):
    def __init__(self,
                 fmt: str = None,
                 datefmt: str = None,
                 style: str = ...,
                 log_colors: _colormap = ...,
                 reset: bool = ...,
                 secondary_log_colors: Dict[str, _colormap] = ...) -> None: ...
```

---

# Writing Stub Files

Writing a stub file is fairly easy:

* Find the library documentation

* Copy-paste function signatures from there

* Adapt them to be real Python code

--

Stubs can be small or large:

* For small modules, it's normally easy to make a complete stub

* For bigger libraries, you can start with what you need

---

# Typeshed

Mypy comes with a repository of stub files called Typeshed:

* Stub files for almost all stdlib modules

* Stub files for some third-party modules (`requests`, `six`, `lxml`, ...)

* See https://github.com/python/typeshed — pull requests welcome!

---

template: inverse

# Problems and Bugs

---

# Problems

This new world is not without its problems:

* Syntax can become very verbose:

    ```python
    def _robust_get(get_func: Callable[[Dict[str, Any]], List[Dict[str, str]]],
                    time_from: pd.Timestamp,
                    time_till: pd.Timestamp,
                    limit: int,
                    arg: Dict[str, Any]) -> List[Dict[str, str]]:
        """Get data between time_from and time_till."""
        pass
    ```

    * However, you save space in your docstrings

    * Type aliases help here

--

* Overhead of maintaining type information

    * You might have ended up spending that time anyway fixing bugs

    * Battling the type system can be a sign of bad design

---

# Bugs

Mypy is still a young projet:

* There are various bugs in the type checker

* Some features of PEP 484 are not yet implemented

---

template: inverse

# Conclusions

---

# Optional Typing Checking Works

After using it for five months at Rackspace:

* Refactoring can be done with greater confidence

* Stupid bugs are caught earlier

* The overhead of writing stub files seems acceptable

* Blending typed and untyped code works well

It's a little bleeding edge, but it's fun to be a pioneer!

---

template: inverse

# Thanks!
