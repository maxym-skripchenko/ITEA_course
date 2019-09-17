import re


string = 'asdf fjdk;afed,fjek,asdf,foo'
print(string)

string1 = string.replace(";", ",").replace(" ", ";").replace("asdf,", "asdf ", 1)
print(string1)
