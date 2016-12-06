import resource
import socket
from urllib.parse import urlparse

from loop import Loop
loop = Loop()

connection_count = 0


async def echo(sock):
    global connection_count
    while True:
        data = await loop.sock_recv(sock, 1024)
        if not data:
            break
        await loop.sock_sendall(sock, b'Echo: ' + data)
    print('Connection', connection_count, 'closed')
    connection_count -= 1


async def listen(address):
    global connection_count
    server_sock = socket.socket()
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind(address)
    server_sock.listen()
    server_sock.setblocking(False)

    while True:
        client_sock, addr = await loop.sock_accept(server_sock)
        connection_count += 1
        print('Connection', connection_count, 'from', addr)
        loop.create_task(echo(client_sock))


if __name__ == '__main__':
    soft, hard = resource.getrlimit(resource.RLIMIT_NOFILE)
    print('Setting max number of open files to', hard)
    resource.setrlimit(resource.RLIMIT_NOFILE, (hard, hard))

    print('Starting echo server')
    loop.create_task(listen(('', 25000)))
    try:
        loop.run()
    except KeyboardInterrupt:
        print('Stopping echo server')
