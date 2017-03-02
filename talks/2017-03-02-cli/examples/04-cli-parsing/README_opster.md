Usage examples for the Opster implementation
============================================

```console
    $ report_opster.py
    usage: report_opster.py <command> [options]
    
    commands:
    
     generate  Generate a report.
     help      Show help for a given help topic or a help overview.
     list      List available reports.
```

```console
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

```console
    $ report_opster.py list --help
    report_opster.py list [OPTIONS]
    
    List available reports.
    
    options:
    
        --experimental  include experimental reports
     -h --help          display help
```

```console
    $ report_opster.py list
    customers
    sales
```

```console
    $ report_opster.py generate sales --notify somebody --notify anybody
    Generate sales report over 1 periods in text format: /dev/stdout
    Notify that report is ready: somebody, anybody
```

```console
    $ report_opster.py generate customers --format html
    Generate customers report over 1 periods in html format: /dev/stdout
    No notifications to be sent.
```

```console
    $ report_opster.py generate customers --format csv
    error: unrecognised value: 'csv' (should be one of text, html)
    
    report_opster.py generate [OPTIONS] NAME
    
    Generate a report.
    
    options:
    
     -o --output   the output file (default: /dev/stdout)
     -p --periods  the number of periods (default: 1)
     -f --format   the format of the report (default: text)
        --notify   email address (can be repeated)
     -h --help     display help
    [255]
```

```console
    $ report_opster.py generate inventory
    Invalid report name: inventory
    [255]
```
