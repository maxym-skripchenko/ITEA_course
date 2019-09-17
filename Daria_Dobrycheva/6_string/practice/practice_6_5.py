import re

#Return last word from string. result: India

result = re.findall(r'\w+$', 'AV is largest Analytics community of India')
print (result)



