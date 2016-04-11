from twisted.internet import defer, reactor
from twisted.web.client import getPage

@defer.inlineCallbacks
def printResult():
	html = yield getPage("http://python.org")
	print(html)
	reactor.stop()

printResult()
reactor.run()
