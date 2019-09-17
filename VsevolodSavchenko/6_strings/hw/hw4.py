import re
string = "asdf fjdk;afed,fjek,asdf,foo"

result= re.split(r"[;,\s]", string)

print(result)