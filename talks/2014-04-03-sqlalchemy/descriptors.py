import weakref


class DBProperty(object):
    def __init__(self):
        self.data = weakref.WeakKeyDictionary()

    def __get__(self, instance, owner):
        print '*** querying database for', instance
        if instance not in self.data:
            raise AttributeError('not set')
        return self.data[instance]

    def __set__(self, instance, value):
        print '*** saving', value, 'to database'
        self.data[instance] = value

    def __delete__(self, instance):
        print '*** deleting', instance, 'from database'
        self.deleted[instance] = True


class Book(object):
    title = DBProperty()
    pages = DBProperty()

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

class VerboseField(object):
    def __init__(self, name):
        self.data = weakref.WeakKeyDictionary()
    def __get__(self, instance, owner):
        print '*** reading field'
        return self.data[instance]
    def __set__(self, instance, value):
        print '*** setting field to', value
        self.data[instance] = value

class Foo(object):
    x = VerboseField('field')


if __name__ == '__main__':
    c = Customer()
    print c.phone
