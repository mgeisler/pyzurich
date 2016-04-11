from twisted.internet import reactor
from twisted.web.client import getPage

def printResult(html):
    print(html)
    reactor.stop()

def printError(err):
    print("Unable to fetch")
    reactor.stop()

d = getPage("http://not-python.org")
d.addCallback(printResult)
d.addErrback(printError)

reactor.run()
