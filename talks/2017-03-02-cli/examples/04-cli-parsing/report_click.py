#! /usr/bin/env python

import click
from report import Report

@click.group()
def main():
    pass

@main.command()
@click.option('--experimental', is_flag=True, help='Include experimental reports')
def list(experimental):
    """List available reports."""
    for k in Report.list():
        print(k)

@main.command()
@click.argument('name')
@click.option('--output' , '-o', help='The output file', default='/dev/stdout')
@click.option('--periods', '-p', help='The number of periods', default=1)
@click.option('--format' , '-f', help='The format of the report', default='text', type=click.Choice(['text', 'html']))
@click.option('--notify' ,       help='Email address (can be repeated)', multiple=True)
def generate(name, output, periods, format, notify):
    """Generate a report."""
    try:
        report = Report(name, periods)
    except Exception as ex:
        raise click.UsageError(ex)
    report.generate(format, output)
    report.notify(notify)

if __name__ == '__main__':
    main()
