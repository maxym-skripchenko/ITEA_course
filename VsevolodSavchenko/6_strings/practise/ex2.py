def is_palindrome(string):
    return string == string[::-1]


print(is_palindrome("madam"))
print(is_palindrome("radar"))
print(is_palindrome("abcde"))

