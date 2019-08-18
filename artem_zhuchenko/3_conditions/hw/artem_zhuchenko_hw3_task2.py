# Input: credit card number (fake data), cvv, mm/yy

user_input_credit_card_number = input("Card number: ")
user_input_cvv = input("CVV (3 digits): ")
user_input_expiry_date = input(f"Expiry date(mm/yy): ")


import sys

# Check that credit card number length has 16 symbols in other case call exit()

if len(user_input_credit_card_number) != 16:
    sys.exit("Incorrect submission (card number)")

# Try to make credit card number to int() if error output "OK", in other case call exit()

try:
    user_input_credit_card_number = int(user_input_credit_card_number)
except ValueError:
    sys.exit("Incorrect submission (card number)")
else:
    print("OK")
    pass


# Check length of cvv if less than 3 symbols, print error and call exit()


if len(user_input_cvv) < 3:
    sys.exit("Incorrect submission (CVV)")
else:
    pass

# If all checks passed print "Everything fine
print("Everything's fine!")
