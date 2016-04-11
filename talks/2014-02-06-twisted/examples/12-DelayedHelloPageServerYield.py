from twisted.internet import defer, reactor
from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet.task import deferLater
from twisted.web.server import NOT_DONE_YET

class DelayedHelloPage(Resource):
    isLeaf = True
    
    @defer.inlineCallbacks
    def _delayedRender(self, request):
        yield deferLater(reactor, 5, lambda: request)
        request.write("<html><body>Hello Twisted... finally!</body></html>")
        request.finish()

    def render_GET(self, request):
        self._delayedRender(request)
        return NOT_DONE_YET
    
resource = DelayedHelloPage()
factory = Site(resource)
reactor.listenTCP(8080, factory)
print("Listening on port 8080")
reactor.run()
