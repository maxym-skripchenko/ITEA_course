def palindrome(a):
    if a[0:len(a)//2] == a[len(a):len(a)//2:-1]:
        return True
    else:
        return False

string = input("What is your string?: ")
print(palindrome(string))