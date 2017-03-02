Usage examples for the Click implementation
===========================================

```console
    $ export LC_ALL=en_IE.UTF-8
    $ report_click.py
    Usage: report_click.py [OPTIONS] COMMAND [ARGS]...
    
    Options:
      --help  Show this message and exit.
    
    Commands:
      generate  Generate a report.
      list      List available reports.
```

```console
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

```console
    $ report_click.py list --help
    Usage: report_click.py list [OPTIONS]
    
      List available reports.
    
    Options:
      --experimental  Include experimental reports
      --help          Show this message and exit.
```

```console
    $ report_click.py list
    customers
    sales
```

```console
    $ report_click.py generate --notify somebody --notify anybody sales
    Generate sales report over 1 periods in text format: /dev/stdout
    Notify that report is ready: somebody, anybody
```

```console
    $ report_click.py generate --format html customers
    Generate customers report over 1 periods in html format: /dev/stdout
    No notifications to be sent.
```

```console
    $ report_click.py generate --format csv customers
    Usage: report_click.py generate [OPTIONS] NAME
    
    Error: Invalid value for "--format" / "-f": invalid choice: csv. (choose from text, html)
    [2]
```

```console
    $ report_click.py generate inventory
    Usage: report_click.py generate [OPTIONS] NAME
    
    Error: Invalid report name: inventory
    [2]
```
