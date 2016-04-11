from twisted.web.server import Site
from twisted.web.static import File
from twisted.internet import reactor

resource = File('.')
factory = Site(resource)

reactor.listenTCP(8080, factory)
print("Listening on port 8080")
reactor.run()
