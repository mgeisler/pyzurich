import socket
from urllib.parse import urlparse

from loop import Loop

loop = Loop()

async def connect(host):
    sock = socket.socket()
    sock.setblocking(False)
    await loop.sock_connect(sock, (host, 80))
    return sock

async def get(host):
    request = (b"GET / HTTP/1.1\r\n"
               b"Host: " + host.encode('ascii') + b"\r\n"
               b"Connection: close\r\n"
               b"\r\n")

    sock = await connect(host)
    await loop.sock_sendall(sock, request)

    chunks = []
    while True:
        chunks.append(await loop.sock_recv(sock, 4096))
        if not chunks[-1]:  # Server closed connection
            break

    sock.close()
    return b"".join(chunks)

async def download_one(host):
    data = await get(host)
    print("%-24s %3d KB" % (host + ":", len(data) // 1024))

async def download_all(*hosts):
    for host in hosts:
        await download_one(host)

if __name__ == '__main__':
    hosts = ['www.nzz.ch', 'www.20min.ch', 'www.blick.ch',
             'www.bbc.com', 'www.thetimes.co.uk',
             'www.independent.co.uk', 'www.telegraph.co.uk',
             'www.nytimes.com', 'www.latimes.com',
             'www.usatoday.com', 'www.wsj.com',
             'www.srf.ch', 'www.telezueri.ch',
             'www.google.ch', 'www.bing.com']
    loop.create_task(download_all(*hosts))
    loop.run()
