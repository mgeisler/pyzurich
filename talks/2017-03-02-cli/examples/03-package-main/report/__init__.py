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
