import urllib2

response = urllib2.urlopen('http://python.org/')
html = response.read()
print(html)
