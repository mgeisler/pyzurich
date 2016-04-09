import sqlite3


class Customer:
    def __init__(self, name, phone, rowid=None):
        self.name = name
        self.phone = phone
        self.rowid = rowid

    def __repr__(self):
        return 'Customer(%r, %r, %r)' % (self.rowid, self.name, self.phone)

    @classmethod
    def load(cls, conn, rowid):
        cur = conn.execute('SELECT name, phone FROM Customers WHERE rowid = ?',
                           (rowid,))
        row = cur.fetchone()
        return cls(row['name'], row['phone'], rowid)

    def save(self, conn):
        cur = conn.cursor()
        if self.rowid is None:
            cur.execute('INSERT INTO Customers (name, phone) '
                        'VALUES (?, ?)',
                        (self.name, self.phone))
            self.rowid = cur.lastrowid
        else:
            cur.execute('UPDATE Customers SET name = ?, phone = ? '
                        'WHERE rowid = ?',
                        (self.name, self.phone, self.rowid))
        conn.commit()

    def orders(self, conn):
        sql = ('SELECT '
               '  Orders.rowid, Orders.date, '
               '  Items.rowid, Items.name, Items.price '
               'FROM Orders '
               '  JOIN OrderItems ON Orders.rowid = OrderItems.orderid '
               '  JOIN Items ON OrderItems.itemid = Items.rowid '
               'WHERE Orders.customerid = ?')
        results = []
        order_rowid = None
        for row in conn.execute(sql, (self.rowid,)):
            if order_rowid != row[0]:
                order = Order(date=row[1], customer=self, rowid=row[0])
                results.append(order)
                order_rowid = row[0]
            order.items.append(Item(name=row[3], price=row[4], rowid=row[2]))
        return results


class Order:
    def __init__(self, date, customer, rowid=None):
        self.date = date
        self.customer = customer
        self.rowid = rowid
        self.items = []

    def __repr__(self):
        return 'Order(%r, %r, %r)' % (self.date, self.customer, self.rowid)

    @classmethod
    def load(cls, conn, rowid):
        cur = conn.execute('SELECT date, customer FROM Orders WHERE rowid = ?',
                           (rowid,))
        row = cur.fetchone()
        return cls(row['date'], Customer.load(row['customer']), rowid)

    def save(self, conn):
        cur = conn.cursor()
        if self.rowid is None:
            cur.execute('INSERT INTO Orders (date, customerid) VALUES (?, ?)',
                        (self.date, self.customer.rowid))
            self.rowid = cur.lastrowid
        else:
            cur.execute('UPDATE Orders SET date = ?, customerid = ? '
                        'WHERE rowid = ?',
                        (self.date, self.customer.rowid, self.rowid))
        conn.commit()

    def add_item(self, conn, item):
        self.items.append(item)
        conn.execute('INSERT INTO OrderItems (orderid, itemid) VALUES (?, ?)',
                     (self.rowid, item.rowid))


class Item:
    def __init__(self, name, price, rowid=None):
        self.name = name
        self.price = price
        self.rowid = rowid

    @classmethod
    def load(cls, conn, rowid):
        cur = conn.execute('SELECT name, price FROM Items WHERE rowid = ?',
                           (rowid,))
        row = cur.fetchone()
        return cls(row['name'], row['price'], rowid)

    def save(self, conn):
        cur = conn.cursor()
        if self.rowid is None:
            cur.execute('INSERT INTO Items (name, price) VALUES (?, ?)',
                        (self.name, self.price))
            self.rowid = cur.lastrowid
        else:
            cur.execute('UPDATE Items SET name = ?, price = ? WHERE rowid = ?',
                        (self.name, self.price, self.rowid))
        conn.commit()

def open_db(path):
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables(conn):
    conn.execute('CREATE TABLE Customers (name text, phone text)')
    conn.execute('CREATE TABLE Orders (date text, customerid int)')
    conn.execute('CREATE TABLE OrderItems (orderid int, itemid int)')
    conn.execute('CREATE TABLE Items (name text, price real)')
    conn.commit()


def load_customers(conn):
    customers = []
    for row in conn.execute('SELECT rowid, name, phone FROM Customers'):
        customer = Customer(row['rowid'], row['name'], row['phone'])
        customers.append(customer)
    return customers



if __name__ == "__main__":
    conn = open_db(':memory:')
    create_tables(conn)

    c = Customer('Martin', '078 1234 56 78')
    c.save(conn)
    print c

    o = Order('2014-04-01', c)
    o.save(conn)
    print o

    i1 = Item('White Shirt', 10)
    i1.save(conn)

    i2 = Item('Blue Jeans', 20)
    i2.save(conn)

    print c.orders(conn)

    o.add_item(conn, i1)
    print c.orders(conn)
