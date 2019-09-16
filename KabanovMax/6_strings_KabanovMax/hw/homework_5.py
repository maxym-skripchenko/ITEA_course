def valid_phone_number(phone):
	if len(phone) == 13 and phone[0:4] == '+380':
		print('Phone is valid')
	else:
		print('Phone is not valid')


phone = (input("Your phone number: "))


