import pprint
import python_module

text = open('/usr/share/common-licenses/BSD').read()
counts = python_module.word_count(text)
pprint.pprint(counts)
