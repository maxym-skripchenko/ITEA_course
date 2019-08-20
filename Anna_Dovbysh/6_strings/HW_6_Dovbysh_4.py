import re
my_string = 'asdf fjdk;afed,fjek,asdf,foo'
print (re.findall(r"[\w']+", my_string))