import sys
sys.path.append("/Users/artem/storage/itea/ITEA_course/artem_zhuchenko/6_strings/practise")

from artem_zhuchenko_6pr_ex1 import generate_n_chars

assert isinstance((generate_n_chars(4, "n")), str) == True, "should return string"
assert generate_n_chars(6, "n") == "nnnnnn", "should multiply characters"
assert generate_n_chars(8, "l") == "llllllll", "should multiply characters"


