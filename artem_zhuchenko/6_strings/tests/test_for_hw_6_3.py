import sys
sys.path.append("/Users/artem/storage/itea/ITEA_course/artem_zhuchenko/6_strings/hw")

from hw6_3 import filter_long_words

assert (isinstance
        (filter_long_words(["artem", "katya", "olya", "pete", "tom", "sam"], 4), list)) == True, "Should return list!"
assert filter_long_words([], 4) is None, "should return None with empty list"
assert filter_long_words(["5656", "539853", "5953"], 4) == ["539853"], "word can be composed of digits too!"