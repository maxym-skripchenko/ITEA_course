import sys
sys.path.append("/Users/artem/storage/itea/ITEA_course/artem_zhuchenko/6_strings/practise")

from artem_zhuchenko_6pr_ex3 import overlapping

["9", "8", "7"]


assert (isinstance(overlapping([9, 8, 7], ["a", "b", "c"]), bool)) == True, "should return bool"
assert overlapping([9, 8, 7], [1, 2, 9]) == True, "should return True"