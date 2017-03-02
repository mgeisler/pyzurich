name: inverse
layout: true
class: center, middle, inverse

---

# Writing command-line programs in Python

Stefano Taschini

taschini@gmail.com

2017-03-02 PyZurich

---

layout: false

# About me

* My name is Stefano Taschini.

--

* Using Python since immemorable time.

--

* Literally: I cannot remember when I started using Python.

--

* Using Python in a professional capacity since 2007.

--

* Currently a business intelligence specialist at Centralway Numbrs AG.

  * _[We're hiring!](https://www.centralway.com/uk/careers/open-positions)_

---

# About the talk

* Loosely inspired by the "Web micro-framework battle" by Richard Jones.

* Exercise: Add CLI to access the functionalities provided by a Python
  library developed in-house.

    * In this case: a mock reporting library.

* File layout

* Command-line parsing

* Testing

---

# Basics

* If the code for the whole library lives in one file, say `library.py`:

    ```python
    #! /usr/bin/env python

    class Report(object):
        pass

    def main():
        print("Using the report class")

    if __name__ == '__main__':
        main()
    ```

* On Unix-like systems:

    ```bash
    $ chmod a+x library.py
    $ ./library.py
    Using the report class
    ```

---

# A more realistic layout

```bash
$ tree report
report
|-- __init__.py
`-- test
    |-- __init__.py
    `-- test_report.py
```

Three possibilities:

1. Put a runnable script in a separate file;
2. Add a `__main__.py` file to the library package;
3. Use a `console_scripts` entry point in `setup.py`.

---

# 1. Separate script

* `run_report.py`:

    ```python
    #! /usr/bin/env python

    from report import Report

    def main():
        print("Using the report class")

    if __name__ == '__main__':
        main()
    ```
--

* `setup.py`:

    ```python
    from setuptools import setup

    setup(
        name='example-02-separate-script',
        version='1.0.0.dev0',
        packages=['report'],
        scripts=['run_report.py'])
    ```

---

# 2. Package main

* `report/__main__.py`:

    ```python
    from . import Report

    def main():
        print("Using the report class")

    if __name__ == '__main__':
        main()
    ```

* Invocation:

    ```bash
    $ python -m report
    Using the report class
    ```

---

# 3. Console script entry point

* `setup.py`:

    ```python
    from setuptools import setup

    setup(
        name='example-03-package-main',
        version='1.0.0.dev0',
        packages=['report'],
        entry_points = {
            'console_scripts': ['report=report.__main__:main'],
        }
    )
    ```

* Console:

    ```bash
    $ pip install -e .
    $ report
    Using the report class
    $ pip uninstall -y example-03-package-main
    ```
---

# My personal recommendation

* Use 2 and 3 together:

    ```python
    # report/__main__.py
    from . import Report

    def main():
        print("Using the report class")

    if __name__ == '__main__':
        main()
    ```

    ```python
    # setup.py
    from setuptools import setup

    setup(
        name='example-03-package-main',
        version='1.0.0.dev0',
        packages=['report'],
        entry_points = {
            'console_scripts': ['report=report.__main__:main'],
        }
    )
    ```

---

# My personal recommendation

* Layout:

    ```bash
    $ tree .
    .
    |-- report
    |   |-- __init__.py
    |   |-- __main__.py
    |   `-- test
    |       |-- __init__.py
    |       `-- test_report.py
    `-- setup.py
    ```
* Pro:
  * Encapsulation: all the code is in the package;
  * Works both as installed or uninstalled library;
  * It is cleanly uninstalled by `pip`;

* Feel free to disagree!

* __However__, to evaluates alternative CLI parsing libraries it is
  easeier to use separate scripts.

---

# The Report class

```python
class Report(object):

    _names = ['customers', 'sales']

    def __init__(self, name, periods):
        assert name in self._names, "Invalid report name: {}".format(name)
        self.name = name
        self.periods = periods

    def generate(self, format, output):
        print("Generate {} report over {} periods in {} format: {}".format(
            self.name, self.periods, format, output))

    def notify(self, recipients):
        if recipients:
            print("Notify that report is ready: " + (', '.join(recipients)))
        else:
            print("No notifications to be sent.")

    @classmethod
    def list(cls):
        return cls._names

```

---

# Using the Report class:

```python
>>> Report.list()
['customers', 'sales']

>>> r = Report('customers', 3)

>>> r = Report('inventory', 3)
Traceback (most recent call last)
...
AssertionError: Invalid report name: inventory

>>> r.generate('html', 'report.html')
Generate customers report over 3 periods in html format: report.html

>>> r.notify(['somebody@example.com'])
Notify that report is ready: somebody@example.com

```

---

# CLI Requirements

* Expose the list command:

    ```bash
    $ report.py list
    customers
    sales
    ```

* Expose the generate command:

    ```bash
    $ report.py generate --format html customers
    Generate customers report over 1 periods in html format: /dev/stdout
    No notifications to be sent.
    ```

* Provide usage info:

    ```bash
    $ report.py
    Usage: report.py [OPTIONS] COMMAND [ARGS]...

    Commands:
      generate  Generate a report.
      help      Show help for a given help topic or a help overview.
      list      List available reports.
    ```

---

# Opster

* `report_opster.py`:

```python
#! /usr/bin/env python
from opster import command, dispatch
from report import Report

@command()
def generate(
        name,
        output  =('o',    '/dev/stdout', "the output file"),
        periods =('p',                1, "the number of periods"),
        format  =('f', ('text', 'html'), "the format of the report"),
        notify  =( '',               [], "email address (can be repeated)"),
):
    """Generate a report."""
    try:
        report = Report(name, periods)
    except Exception as ex:
        raise command.Error(ex)
    report.generate(format, output)
    report.notify(notify)

# continues...
```

---

# Opster (continued)

```python
@command()
def list(
        experimental=('', False, "include experimental reports"),
):
    """List available reports."""
    for k in Report.list():
        print(k)

if __name__ == '__main__':
    import sys
    sys.exit(dispatch())
```

```bash
$ pip install opster
$ ./report_opster.py
usage: report_opster.py <command> [options]

commands:

 generate  Generate a report.
 help      Show help for a given help topic or a help overview.
 list      List available reports.
```

---

# Click

```python
import click
from report import Report

@click.group()
def main():
    pass

@main.command()
@click.argument('name')
@click.option('--output' , '-o', help='The output file', default='/dev/stdout')
@click.option('--periods', '-p', help='The number of periods', default=1)
@click.option('--format' , '-f', help='The format of the report',
              default='text', type=click.Choice(['text', 'html']))
@click.option('--notify' ,       help='Email address (can be repeated)',
              multiple=True)
def generate(name, output, periods, format, notify):
    """Generate a report."""
    try:
        report = Report(name, periods)
    except Exception as ex:
        raise click.UsageError(ex)
    report.generate(format, output)
    report.notify(notify)

# continues...
```

---

# Click (continued)

```python
@main.command()
@click.option('--experimental', is_flag=True, help='Include experimental reports')
def list(experimental):
    """List available reports."""
    for k in Report.list():
        print(k)

if __name__ == '__main__':
    main()
```

```bash
$ pip install click
$ LC_ALL=en_IE.UTF-8 ./report_click.py
Usage: report_click.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  generate  Generate a report.
  list      List available reports.
```

---

# Testing with Cram

* example.md:

    ~~~markdown
    Example
    =======

        ```
        $ report_opster.py
        usage: report_opster.py <command> [options]

        commands:

         generate  Generate a report.
         help      Show help for a given help topic or a help overview.
         list      List available reports.
        ```

    ~~~

* Run the tests:

    ```bash
    $ pip install cram
    $ cram --indent 4 example.md
    ```

---

# Opster vs Click: no arguments

```bash
    $ report_opster.py
    usage: report_opster.py <command> [options]

    commands:

     generate  Generate a report.
     help      Show help for a given help topic or a help overview.
     list      List available reports.
```

```bash
    $ export LC_ALL=en_IE.UTF-8
    $ report_click.py
    Usage: report_click.py [OPTIONS] COMMAND [ARGS]...

    Options:
      --help  Show this message and exit.

    Commands:
      generate  Generate a report.
      list      List available reports.
```

---

# Opster vs Click: command help

```bash
    $ report_opster.py generate --help
    report_opster.py generate [OPTIONS] NAME

    Generate a report.

    options:

     -o --output   the output file (default: /dev/stdout)
     -p --periods  the number of periods (default: 1)
     -f --format   the format of the report (default: text)
        --notify   email address (can be repeated)
     -h --help     display help
```

```bash
    $ report_click.py generate --help
    Usage: report_click.py generate [OPTIONS] NAME

      Generate a report.

    Options:
      -o, --output TEXT         The output file
      -p, --periods INTEGER     The number of periods
      -f, --format [text|html]  The format of the report
      --notify TEXT             Email address (can be repeated)
      --help                    Show this message and exit.
```

---

# Opster vs Click: running commands

```bash
    $ report_opster.py generate sales --notify somebody --notify anybody -f html
    Generate sales report over 1 periods in html format: /dev/stdout
    Notify that report is ready: somebody, anybody
```

```bash
    $ report_click.py generate --notify somebody --notify anybody -f html sales
    Generate sales report over 1 periods in html format: /dev/stdout
    Notify that report is ready: somebody, anybody
```

* Invalid report name:

```bash
    $ report_opster.py generate inventory
    Invalid report name: inventory
    [255]
```

```bash
    $ report_click.py generate inventory
    Usage: report_click.py generate [OPTIONS] NAME

    Error: Invalid report name: inventory
    [2]
```
