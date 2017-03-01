import pytest
from .. import Report


def test_report_list():
    assert Report.list() == ['customers', 'sales']


def test_report_failinit():
    with pytest.raises(Exception) as ex:
        Report('foo', periods=1)
    assert str(ex.value) == 'Invalid report name: foo'


def test_report_generate(capsys):
    Report('sales', periods=3).generate('html', 'foo.txt')
    out, err = capsys.readouterr()
    assert err == ''
    assert out == \
        'Generate sales report over 3 periods in html format: foo.txt\n'


def test_report_notify_users(capsys):
    Report('customers', periods=2).notify(['nobody@example.net'])
    out, err = capsys.readouterr()
    assert err == ''
    assert out == 'Notify that report is ready: nobody@example.net\n'


def test_report_no_notifications(capsys):
    Report('customers', periods=2).notify([])
    out, err = capsys.readouterr()
    assert err == ''
    assert out == 'No notifications to be sent.\n'
