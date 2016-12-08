import socket
import resource
from urllib.parse import urlparse

from loop import Loop
loop = Loop()


async def connect(address):
    sock = socket.socket()
    sock.setblocking(False)
    await loop.sock_connect(sock, address)
    return sock


async def start_client(i, address):
    sock = await connect(address)
    await loop.sock_sendall(sock, b'Hello from client %d!' % i)
    reply = await loop.sock_recv(sock, 1024)
    print('Client', i, 'got:', reply)
    # Keep client alive with a read that never returns
    await loop.sock_recv(sock, 1024)


async def start_clients(address):
    for i in range(5000):
        loop.create_task(start_client(i, address))


if __name__ == '__main__':
    soft, hard = resource.getrlimit(resource.RLIMIT_NOFILE)
    print('Setting max number of open files to', hard)
    resource.setrlimit(resource.RLIMIT_NOFILE, (hard, hard))

    print('Starting echo clients')
    loop.create_task(start_clients(('localhost', 25000)))
    try:
        loop.run()
    except KeyboardInterrupt:
        print('Stopping echo clients')
