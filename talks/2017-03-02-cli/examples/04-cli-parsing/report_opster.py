#! /usr/bin/env python

from opster import command, dispatch
from report import Report

@command()
def list(
        experimental=('', False, "include experimental reports"),
):
    """List available reports."""
    for k in Report.list():
        print(k)

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

if __name__ == '__main__':
    import sys
    sys.exit(dispatch())
