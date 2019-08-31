import re

line = 'asdf fjdk;afed,fjek,asdf,foo'

result= re.split(r'[;,\s]', line)

print (result)
