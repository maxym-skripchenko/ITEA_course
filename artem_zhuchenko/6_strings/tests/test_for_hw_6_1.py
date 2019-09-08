import sys
sys.path.append(sys.path.append("/Users/artem/storage/itea/ITEA_course/artem_zhuchenko/6_strings/hw"))

from hw6 import words_to_integers


assert (isinstance
        (words_to_integers(["one", "two", "three"]), str)) == False, "Should return list!"
assert words_to_integers(["four", "five", "six"]) == [4, 4, 3], "should return list of lenghts"
assert words_to_integers(["5656", "539853", "5953"]) == [4, 6, 4], "word can be composed of digits too!"