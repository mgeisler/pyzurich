import socket
import types
import collections
import selectors

@types.coroutine
def read_wait(sock):
    yield 'read_wait', sock

@types.coroutine
def write_wait(sock):
    yield 'write_wait', sock

class Loop:
    def __init__(self):
        self.ready = collections.deque()
        self.selector = selectors.DefaultSelector()

    async def sock_connect(self, sock, address):
        await read_wait(sock)
        try:
            sock.connect(address)
        except BlockingIOError:
            pass

    async def sock_accept(self, sock):
        await read_wait(sock)
        return sock.accept()

    async def sock_recv(self, sock, maxbytes):
        await read_wait(sock)
        return sock.recv(maxbytes)

    async def sock_sendall(self, sock, data):
        while data:
            await write_wait(sock)
            nsent = sock.send(data)
            data = data[nsent:]

    def create_task(self, coro):
        self.ready.append(coro)

    def run(self):
        while True:
            if not self.ready:
                if len(self.selector.get_map()) == 0:
                    self.selector.close()
                    return
                for key, events in self.selector.select():
                    self.ready.append(key.data)
                    self.selector.unregister(key.fileobj)

            while self.ready:
                self.current_task = self.ready.popleft()
                try:
                    op, *args = self.current_task.send(None)
                    getattr(self, op)(*args)
                except StopIteration:  # Done with this task
                    pass

    def read_wait(self, sock):
        self.selector.register(sock, selectors.EVENT_READ, self.current_task)

    def write_wait(self, sock):
        self.selector.register(sock, selectors.EVENT_WRITE, self.current_task)
