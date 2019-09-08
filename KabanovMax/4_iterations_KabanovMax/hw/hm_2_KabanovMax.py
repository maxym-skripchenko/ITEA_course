'''
Homework #2 KabanovMax
'''

# Setting end print
sample_output = []

# Dividing Fizz, Buzz, FizzBuzz and adding results in end sample
for number in range(1, 50):
	if number % 3 == 0 and number % 5 == 0:
		sample_output.append("FizzBuzz")
	elif number % 3 == 0:
		sample_output.append("Fizz")
	elif number % 5 == 0:
		sample_output.append("Buzz")
	else:
		sample_output.append(number)

print(sample_output)

'''
End of Homework #2
'''