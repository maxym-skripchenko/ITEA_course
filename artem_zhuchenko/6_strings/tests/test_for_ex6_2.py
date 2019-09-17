import sys
sys.path.append("/Users/artem/storage/itea/ITEA_course/artem_zhuchenko/6_strings/practise")


from artem_zhuchenko_6pr_ex2 import is_palindrome

assert (isinstance(is_palindrome("radar"), bool)) == True, "should return bool"
assert is_palindrome("553355") == True, "should work for numbers"
assert is_palindrome("поророп") == True, "should work for cyrillic"
assert is_palindrome("...,,,...") == True, "should work for commas and dots"
assert is_palindrome("random_string") == False, "should be false"


