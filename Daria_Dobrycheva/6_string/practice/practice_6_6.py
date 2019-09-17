import re

#Get two symbols of each word in string result: ['AV', 'is', 'la', 'An', 'co', 'of', 'In']

result = re.findall(r'\w\w', 'AV is largest Analytics community of India')
print (result)



