import sys
sys.path.append("/Users/artem/storage/itea/ITEA_course/artem_zhuchenko/6_strings/hw")

from hw6_2 import find_longest_word

assert (isinstance
        (find_longest_word(["one", "two", "three"]), int)) == True, "Should return integer!"
assert find_longest_word(["four", "five", "six"]) == 4, "should return the longest when there are more than one"
assert find_longest_word(["5656", "539853", "5953"]) == 6, "word can be composed of digits too!"
