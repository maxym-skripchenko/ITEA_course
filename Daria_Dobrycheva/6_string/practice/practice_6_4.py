import re

#Return first word from string. result: AV

result = re.match(r'AV', 'AV is largest Analytics community of India')
print (result.group(0))



