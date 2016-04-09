name: inverse
layout: true
class: center, middle, inverse

---

# Switch to Python 3 Today!

Martin Geisler  
martin@geisler.net

2016-04-07 — PyZurich

---
layout: false

# Agenda

1. Python History

2. Managing Python Versions

3. Some Changes in Python 3

--

I will not be talking much about how to port code to Python 3

There are many online resources for this, e.g.:

* https://docs.python.org/3/howto/pyporting.html

* http://python3porting.com/noconv.html

---

# Martin Geisler

* Fullstack developer at Rackspace Zurich

* Was active in the Mercurial project

* Have used Python since Python version 1.6 or 2.0 (around 2000)

--

## Rackspace

* Hosting company: ~6,000 employees, 9 data centers around the world

* Started OpenStack with NASA, maybe the largest known Python project

* Supports OpenStack, Amazon AWS, Microsoft Azure

---

# Python 3000, Python 3k, Python 3.0, ...?!

Python 3000 was used as a placeholder for the "next big thing":

> `From: Guido van Rossum`  
> `Subject: Python 2 namespace change?`  
> `Date: 2000-01-20 15:45:40`
>
> > `[...] this would be too big a change for Python 1. Maybe this is
> > something to consider for Python 2?`
>
> `Note: from now on the new name for Python 2 is Python 3000. :-)`

---

# Goals of Python 3

From PEP 3100:

> A general goal is to reduce feature duplication by removing old ways
> of doing things. A general principle of the design will be that one
> obvious way of doing something is enough

---

# Python Major Versions

## Python 1.0 – January 1994

Ancient history. Ran on steam-powered computers?

--

## Python 2.0 – October 16, 2000

The Python we know and love with list comprehensions, the `unicode`
type, methods on `str`, `*args` arguments, `zip` builtin, `+=` syntax,
etc.

--

## Python 3.0 – December 3, 2008

The future of Python with a `print` function, Unicode `str`, `bytes`
for data, `super()` syntax, asyncio, etc. Also comes with Python 2
incompatibility.

---

# Python Release History

* **Python 1.0 – January 1994**
    * Python 1.5 – December 31, 1997
    * Python 1.6 – September 5, 2000

* **Python 2.0 – October 16, 2000**
    * Python 2.1 – April 17, 2001
    * Python 2.2 – December 21, 2001
    * Python 2.3 – July 29, 2003
    * Python 2.4 – November 30, 2004
    * Python 2.5 – September 19, 2006
    * Python 2.6 – October 1, 2008
    * Python 2.7 – July 3, 2010

* **Python 3.0 – December 3, 2008**
    * Python 3.1 – June 27, 2009
    * Python 3.2 – February 20, 2011
    * Python 3.3 – September 29, 2012
    * Python 3.4 – March 16, 2014
    * Python 3.5 – September 13, 2015

---

# Python 2 Status

Perpetual feature freeze.

* Latest release: 2.7.11, December 5, 2015

* Last planned release: 2.7.12 in May 2016

* Python 2.7 end of life: 2020

*Please make sure you're using Python 2.7.10 or later due to important
security updates to the SSL standard library module.*

---

# Python 3 Status

This is where the fun happens!

* All new features go into Python 3

* New standard library modules

* Changes to the language syntax

--

* This cleanup was not done in a backwards-compatible fashion

* This lead to a slow adoption of Python 3

---

# Tracking the Python 3 Uptake

* The 200 most popular projects: https://python3wos.appspot.com/

* The 360 most popular projects: http://py3readiness.org/

* Analyze your own project: https://caniusepython3.com/

---

# PyPI Package Uploads

Python 3 package uploads will soon overtake Python 2 uploads:

![](pypi-updated-package-versions.png)

* Light blue line: packages with Python 3 support.

* Purple line: packages with Python 2 support.

.small[From: https://blogs.msdn.microsoft.com/pythonengineering/2016/03/08/python-3-is-winning/]

---

# PEP 3000: Python 3000

PEP 3000 is a "meta PEP", it describes the process behind Python 3000

Other Python 3 overview PEPs:

* PEP 3099: Things that will Not Change in Python 3000

* PEP 3100: Miscellaneous Python 3.0 Plans

--

## The Gory Details

The concrete ideas are formulated in a large number of other PEPs:

* PEP 3101: Advanced String Formatting

* PEP 3102: Keyword-Only Arguments

* PEP 3104: Access to Names in Outer Scopes

* ...

---

# More PEPs...

* PEP 3105: Make print a function

* PEP 3106: Revamping dict.keys(), .values() and .items()

* PEP 3107: Function Annotations

* PEP 3108: Standard Library Reorganization

* PEP 3109: Raising Exceptions in Python 3000

* PEP 3110: Catching Exceptions in Python 3000

* PEP 3111: Simple input built-in in Python 3000

* PEP 3112: Bytes literals in Python 3000

* PEP 3113: Removal of Tuple Parameter Unpacking

* PEP 3114: Renaming iterator.next() to iterator.\_\_next\_\_()

* PEP 3115: Metaclasses in Python 3000

* PEP 3116: New I/O

* ...

---

# Even More PEPs...

* PEP 3118: Revising the buffer protocol

* PEP 3119: Introducing Abstract Base Classes

* PEP 3120: Using UTF-8 as the default source encoding

* PEP 3123: Making PyObject_HEAD conform to standard C

* PEP 3127: Integer Literal Support and Syntax

* PEP 3129: Class Decorators

* PEP 3131: Supporting Non-ASCII Identifiers

* PEP 3132: Extended Iterable Unpacking

* PEP 3134: Exception Chaining and Embedded Tracebacks

* PEP 3135: New Super

* PEP 3137: Immutable Bytes and Mutable Buffer

* PEP 3138: String representation in Python 3000

* ...

---

# Done!

* PEP 3141: A Type Hierarchy for Numbers

* PEP 3144: IP Address Manipulation Library for the Python ...

* PEP 3147: PYC Repository Directories

* PEP 3148: futures - execute computations asynchronously

* PEP 3149: ABI version tagged .so files

* PEP 3151: Reworking the OS and IO exception hierarchy

* PEP 3154: Pickle protocol version 4

* PEP 3155: Qualified name for classes and functions

* PEP 3156: Asynchronous IO Support Rebooted: the "asyncio" Module

* PEP 3333: Python Web Server Gateway Interface v1.0.1

.small[(That was just the PEPs in the 3*xxx* range, I'm sure other PEPs affect Python 3 too)]

---

template: inverse

# Using Python 3 on a Python 2 system

---

# Virtual Environments

You can specify the Python binary to use when you create a new virtualenv:

```sh
$ virtualenv --python /usr/bin/python3 foo
```

When the virtualenv is activated, `python` will be the correct version:
```sh
$ source foo/bin/activate
(foo)$ python --version
Python 3.5.1+
```

Virtualenvwrapper also accepts `-p` and `--python`.

---

# Managing Python Versions

`pyenv` is a tool that allows you to install your own Python version
```sh
$ pyenv install 2.7.1
$ pyenv install 3.5.1
```
The specified version is compiled and installed below `~/.pyvenv/` by default

--

You can activate a version for your user:
```sh
$ pyenv global 2.7.1
$ python --version
Python 2.7.1
$ pyenv global 3.5.1
$ python --version
Python 3.5.1
```

See https://github.com/yyuu/pyenv

---

template: inverse

# Some of the Changes in Python 3

---

# PEP 3102: Keyword-Only Arguments

A `*` in the argument list indicates that the following arguments must
be passed as keyword arguments:

```python
>>> def foo(x, y, *, kw=None):
...    pass

>>> foo(10, 20, 'hello')
Traceback (most recent call last):
    ...
TypeError: foo() takes 2 positional arguments but 3 were given

```

---

# PEP 3104: Access to Names in Outer Scopes

You can use `nonlocal` to access outer scopes:
```python
>>> def make_counter():
...     count = 0
...     def inc():
...         nonlocal count
...         count += 1
...         return count
...     return inc

>>> counter = make_counter()
>>> counter()
1
>>> counter()
2

```

In Python 2, you'll use `count = [0]` and `count[0] += 1` instead

---

# PEP 3105: Make print a Function

There is now a `print` built-in function. It is no longer a keyword:
```python
>>> writer = print
>>> writer('some log message')
some log message

```

It has keyword arguments for things like the separator:

```python
>>> print(10, 20, 30, sep=' -- ', end='!\n')
10 -- 20 -- 30!

```

---

# PEP 3106: Revamping dict.keys(), .values() and .items()

These methods now return views, not lists. They're like `iterkeys`,
`itervalues`, and `iteritems` in Python 2:

```python
>>> d = {'foo': 10}
>>> d.items()
dict_items([('foo', 10)])
>>> list(d.items())
[('foo', 10)]

```

---

# PEP 3107: Function Annotations

Python 3 introduced support for annotations:
```python
>>> def very_large(n: int) -> bool:
...     return n > 1e9

>>> list(sorted(very_large.__annotations__.items()))
[('n', <class 'int'>), ('return', <class 'bool'>)]

```

This will be covered in the next talk, so please come back on April
28th!

---

# PEP 3110: Catching Exceptions

You can no longer use the `except E, N` syntax, you must use this
style:

```python
>>> try:
...     1 / 0
... except ZeroDivisionError as e:
...     print(e)
division by zero

```

---

# PEP 3112: Bytes literals

You can specify `bytes` objects directly using the `b` prefix on a string:
```python
>>> buf = b"a few bytes: \x00 \x10 \x20"
>>> len(buf)
18

```

---

# PEP 3113: Removal of Tuple Parameter Unpacking

You can no longer unpack tuples directly:

```python
def add((x1, y1), (x2, y2)):
    pass
```

The syntax complicated introspection and was deemed to be unimportant
enough that it could go away. Use normal parameters instead and unpack
the tuples inside your function.

---

# PEP 3115: Metaclasses in Python 3000

Metaclasses can now be specified using a keyword argument:

```python
class Foo(base1, base2, metaclass=mymeta):
   ...

```

This replaces the old `__metaclass__` variable in a class definition.

---

# PEP 3116: New I/O

The I/O system got updated to give a clear definition of what
"file-like" means and what methods you can expect to find on a
file-like object.

---

# PEP 3120: Using UTF-8 as the default source encoding

Python 3 source files use UTF-8 as the default encoding. So this is
now perfectly fine

```python
>>> intro = """
... Python ([ˈpaɪθn̩], [ˈpaɪθɑn], auf Deutsch auch [ˈpyːtɔn]) ist eine
... universelle, üblicherweise interpretierte höhere Programmiersprache.
... """

```

No `# -*- coding: utf-8 -*-` line needed!

---

# PEP 3127: Integer Literal Support and Syntax

Octal numbers and binary numbers:

```python
>>> 0o123
83
>>> 0b10010
18

```

The old `0123` syntax for octal numbers is no longer supported:

```python
>>> 0123
Traceback (most recent call last):
    ...
    0123
       ^
SyntaxError: invalid token

```

---

# PEP 3129: Class Decorators

Classes can be decorated the same way you decorate functions and
methods:

```python
>>> def foo(cls):
...    pass

>>> @foo
... class A:
...     pass

```

---

# PEP 3131: Supporting Non-ASCII Identifiers

Yes, you can now use non-ASCII characters in your identifiers!

The characters must be classified as a letter in the Unicode standard:

```python
>>> π = 3.14
>>> φ = 1.61
>>> π * φ
5.055400000000001

```

---

# PEP 3132: Extended Iterable Unpacking

You can now unpack just some elements from an iterator:

```python
>>> a, b, *rest = range(10)
>>> a
0
>>> b
1
>>> rest
[2, 3, 4, 5, 6, 7, 8, 9]

```

---

# PEP 3135: New Super

You can use `super()` without any arguments to get access to the super
class:

```python
>>> class A:
...     def foo(self):
...        print("This is from A")

>>> class B(A):
...     def foo(self):
...         super().foo()
...         print("This is from B")

>>> b = B()
>>> b.foo()
This is from A
This is from B

```

---

# PEP 3148: futures - execute computations asynchronously

Elegant framework for asynchronous tasks:

```python
>>> from concurrent import futures

>>> def square(n):
...     return n * n

>>> with futures.ThreadPoolExecutor() as executor:
...     results = executor.map(square, [1, 2, 3, 4, 5])
>>> list(results)
[1, 4, 9, 16, 25]

```

---

# PEP 3156: Asynchronous IO Support Rebooted: the "asyncio" Module

Like Twisted, but part of the standard library.

```python
import asyncio

def hello_world(loop):
    print('Hello World')
    loop.stop()

loop = asyncio.get_event_loop()

# Schedule a call to hello_world()
loop.call_soon(hello_world, loop)

# Blocking call interrupted by loop.stop()
loop.run_forever()
loop.close()
```

---

template: inverse

# Conclusions

---

# Start using Python 3 :-)

* Support is widespread

* Python 3 has new cool features

* Start using it for new projects

* Consider moving old projects to Python 3
