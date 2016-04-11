from twisted.internet import defer, reactor
from twisted.web.client import getPage

@defer.inlineCallbacks
def printResult():
    try:
        html = yield getPage("http://not-python.org")
        print(html)
    except Exception:
        print("Unable to fetch.")
    finally:
        reactor.stop()

printResult()
reactor.run()
