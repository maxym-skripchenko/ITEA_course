import re
string = "AV is largest Analytics community of India"

result = re.findall(r"\w+$", "AV is largest Analytics community of India")

print(result)