import re

a = str(["+380971236789", "+380809123232", "99999x9999"])
b = re.findall(r'\S\+38097\d+', a)
print(b)