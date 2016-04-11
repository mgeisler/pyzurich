from twisted.internet import reactor
from twisted.web.client import getPage

def printResult(html):
	print(html)
	reactor.stop()

d = getPage("http://python.org")
d.addCallback(printResult)

reactor.run()
