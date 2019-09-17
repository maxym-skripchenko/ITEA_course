import re

li = str(["+380971236789", "+380809123232", "99999x9999"])
p = re.findall(r'\S\+38097\d+', li)
print(p)