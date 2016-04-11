from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.resource import Resource

class HelloPage(Resource):
    isLeaf = True
    def render_GET(self, request):
        return "<html><body>Hello Twisted</body></html>"

resource = HelloPage()
factory = Site(resource)

reactor.listenTCP(8080, factory)
print("Listening on port 8080")
reactor.run()
