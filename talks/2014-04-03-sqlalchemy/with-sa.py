from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)

from sqlalchemy.orm import sessionmaker, column_property, deferred
Session = sessionmaker(bind=engine)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Table, Column, Integer, String, ForeignKey, Binary
from sqlalchemy.orm import relationship


class Customer(Base):
    __tablename__ = 'Customers'
    rowid = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    orders = relationship('Order')

    def __repr__(self):
        return 'Customer(%r, %r, %r)' % (self.rowid, self.name, self.phone)


order_items = Table('OrderItems', Base.metadata,
                    Column('order_id', Integer, ForeignKey('Orders.rowid')),
                    Column('item_id', Integer, ForeignKey('Items.rowid')))


class Order(Base):
    __tablename__ = 'Orders'
    rowid = Column(Integer, primary_key=True)
    date = Column(String)
    customer_id = Column(Integer, ForeignKey('Customers.rowid'))
    items = relationship("Item", secondary=order_items)

    def __repr__(self):
        return 'Order(%r, %r, %r)' % (self.date, self.rowid, self.items)


class Item(Base):
    __tablename__ = 'Items'
    rowid = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    def __repr__(self):
        return 'Item(%r, %r)' % (self.name, self.price)


class User(Base):
    __tablename__ = 'users'
    user_id = Column('id', Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    name = column_property(firstname + ' ' + lastname)
    photo = deferred(Column(Binary))


if __name__ == "__main__":
    session = Session()
    Base.metadata.create_all(engine)

    c1 = Customer(name='Roy Trenneman', phone='078 123 45 67')
    c2 = Customer(name='Maurice Moss', phone='044 551 10 12')
    session.add(c1)
    session.add(c2)

    o = Order(date='2014-04-01')
    session.add(o)
    c1.orders.append(o)
    print o

    i1 = Item(name='White Shirt', price=10)
    i2 = Item(name='Blue Jeans', price=20)
    session.add(i1)
    session.add(i2)

    o.items.append(i1)
    o.items.append(i2)

    print c1.orders

    u = User(firstname='Jen', lastname='Barber', photo='')
    session.add(u)

    session.query(User).filter_by(name='Jen Barber').one()

    session.flush()
