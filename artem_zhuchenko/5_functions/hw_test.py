import sys
import unittest

# sys.path.append(r'/Users/artem/storage/itea/ITEA_course/artem_zhuchenko/5_functions/hw')

import hw

class My_test(unittest.TestCase):

    def test_my_max_list(self):
        self.assertEqual(my_max_list([2, 5, -1]), 5, "Should return 5!")

    def test_my_max_list_true(self):
        self.assertTrue(my_max_list(["aa", "bbb"]) == "bbb", "Should return longest string!")

    def test_my_max_list_false(self):
        self.assertFalse(my_max_list(my_list) == None, "Should return my_max!")

if __name__ == '__main__':
    unittest.main()
