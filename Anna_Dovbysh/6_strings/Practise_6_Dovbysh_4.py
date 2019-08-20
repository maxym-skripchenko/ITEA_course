import re

my_string = 'AV is largest Analytics community of India'

first_in_my_string = my_string.partition(' ')[0]
print(first_in_my_string) #AV

last_in_my_string = my_string.split(' ')[-1]
print(last_in_my_string) #India

result_two_symb = re.findall(r'\b\w{2}',my_string)
print(result_two_symb) #two symbol of each word