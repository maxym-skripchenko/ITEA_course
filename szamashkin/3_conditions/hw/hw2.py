
#################2. Input: credit card number (fake data), cvv, mm/yy###############
number = input("Enter your credit card: ")
cvv = input("Enter cvv: ")
validity = input("Enter card validity date in mm/yy : ")

####Check that credit card number length has 16 symbols in other case call exit()####
length = len(number)
print(length)
if int(length) == 16:
    print("OK")
else:
    exit(1)
#####Try to make credit card number to int() if error output "OK", in other case call exit()#####
try:
    x = int(number)
except Exception as error:
    exit(1)

#####Check length of cvv if less than 3 symbols, print error and call exit()#####
if len(cvv) == 3:
    print("Error")
else:
    print("OK")

print("Everything is fine")