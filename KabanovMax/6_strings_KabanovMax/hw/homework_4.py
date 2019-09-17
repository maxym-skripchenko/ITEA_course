import re

my_string = 'asdf fjdk;afed,fjek,asdf,foo'

result = re.findall(r"[\w']+", my_string)

print(result)