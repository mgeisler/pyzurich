class MakePrivate(type):
    def __new__(cls, name, bases, attrs):
        private = {}
        for key, value in attrs.iteritems():
            private['_' + key] = value
        return super(MakePrivate, cls).__new__(cls, name, bases, private)

class Foo(object):
    __metaclass__ = MakePrivate
    x = 10

foo = Foo()
print foo._x
