import urllib2

try:
	response = urllib2.urlopen('http://not-python.org/')
	html = response.read()
	print(html)
except Exception:
	print("Unable to fetch.")
