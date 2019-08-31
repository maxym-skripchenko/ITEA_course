#a = "1"
#b = """abc"""
#c = "def"

#d = a + b + c
#print(d)

#ef_in_d = c in d
#print(ef_in_d)


#abc = "abcdefg"
# print(abc[::-1])

# s = 'foobar'
# print(s[::2])

# s = '0123456789'
# print(s[0:6:2])
# print(s[1:9:2])
# print(s[::3])
# print(s[::-1])

# my_list = [1, 2, 3]
#
# my_list[2] = 5
#
# print(my_list)
#
# my_tuple = (1, 2, 3)
# string = "abcde"
# string[4] = "f"
# print(string)
#
# my_string = string[:-1] + f

# string = "my string"
# print(string[6].upper())
#
# print(string.count("a"))

# print(" | ".join(["a", "b", 'c']))
import re
#import re

#pattern = re.compile("ab*", IGNORECASE)


p = re.compile("[\d]")
#p.match("abcd")



m = p.match("Tempo4444")
print(m)