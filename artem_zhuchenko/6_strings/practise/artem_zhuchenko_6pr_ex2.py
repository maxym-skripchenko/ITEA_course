'''Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards).
For example, is_palindrome("radar") should return True.'''

def is_palindrome(some_string):
    return some_string == some_string[::-1]



