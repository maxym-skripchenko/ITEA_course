import sys
import unittest

sys.path.append(r'/Users/artem/storage/itea/ITEA_course/artem_zhuchenko/5_functions/my_modules')

from ex5_1 import my_max

# print(my_max(2, 3))

class My_test(unittest.TestCase):

    def test_my_max(self):
        self.assertEqual(my_max(2, 4), 4, "Should return 4!")

    def test_my_max_true(self):
        self.assertTrue(my_max(3, 8) == 8, "Should return 8!")

    def test_my_max_false(self):
        self.assertFalse(my_max(4, 4) != "Numbers are equal!", "Should return string")

if __name__ == '__main__':
    unittest.main()

