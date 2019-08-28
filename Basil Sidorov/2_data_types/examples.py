# Python 3.7.3 (default, Apr  2 2019, 15:34:40)
# [Clang 10.0.1 (clang-1001.0.46.3)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> variable = 2019
# >>> variable
# 2019
# >>> variable /= 2019
# >>> variable = 2019
# >>> variable != 2019
# False
# >>> variable '; 2019
#   File "<stdin>", line 1
#     variable '; 2019
#                    ^
# SyntaxError: EOL while scanning string literal
# >>> variable = 2019
# KeyboardInterrupt
# >>> letter = "L"
# >>> letter
# 'L'
# >>> my_name = “Yurii”
#   File "<stdin>", line 1
#     my_name = “Yurii”
#                     ^
# SyntaxError: invalid character in identifier
# >>> my_name = 'A"
#   File "<stdin>", line 1
#     my_name = 'A"
#                 ^
# SyntaxError: EOL while scanning string literal
# >>> my_name = 'A'
# >>> my_name = "A"
# >>> True
# True
# >>> False
# False
# >>> type(False)
# <class 'bool'>
# >>> my_bool = True
# >>> type(my_bool)
# <class 'bool'>
# >>> one = 1
# >>> one
# 1
# >>> type(one)
# <class 'int'>
# >>> one_float = 2.01
# >>> one
# one        one_float
# >>> one_float
# 2.01
# >>> one_float = 2.0
# >>> one_float
# 2.0
# >>> one_complex = 2a
#   File "<stdin>", line 1
#     one_complex = 2a
#                    ^
# SyntaxError: invalid syntax
# >>> a = 1
# >>> one_complex = 2a
#   File "<stdin>", line 1
#     one_complex = 2a
#                    ^
# SyntaxError: invalid syntax
# >>> one_complex = 2i
#   File "<stdin>", line 1
#     one_complex = 2i
#                    ^
# SyntaxError: invalid syntax
# >>> one_complex = 2y
#   File "<stdin>", line 1
#     one_complex = 2y
#                    ^
# SyntaxError: invalid syntax
# >>> one_complex = 2x
#   File "<stdin>", line 1
#     one_complex = 2x
#                    ^
# SyntaxError: invalid syntax
# >>> import cmath
# >>> x = 5
# >>> y = 3
# >>> complex(x, y)
# (5+3j)
# >>> my_string = "My string"
# >>> my
# my_bool    my_name    my_string
# >>> my_string
# 'My string'
# >>> my_list = [True, x, one]
# one        one_float
# >>> my_list = [True, x, one_float, one]
# one        one_float
# >>> my_list = [True, x, one_float, one]
# >>> my
# my_bool    my_list    my_name    my_string
# >>> my_list
# [True, 5, 2.0, 1]
# >>> is_programmer = True
# >>> is_programmer
# True
# >>> my_list = [is_programmer, x, one_float, one]
# >>> my_list.append(one)
# >>> my_list
# [True, 5, 2.0, 1, 1]
# >>> my_tuple = (one, is
# is             is_programmer  isinstance(    issubclass(
# >>> my_tuple = (one, is_programmer, x)
# >>> my_set = {one, one, 5, 5, is_programmer, is_programmer}
# >>> my_set
# {1, 5}
# >>> my_set = {one, one, 5, 5, is_programmer, is_pro}
# KeyboardInterrupt
# >>> is_programmer = False
# >>> my_set = {one, one, 5, 5, is_programmer, is_programmer}
# >>> my_set
# {False, 1, 5}
# >>> zero = 0
# >>> my_set = {zero, 5, 5, is_programmer, is_programmer}
# >>> my_set
# {0, 5}
# >>> set()
# set()
# >>> list()
# []
# >>> tuple()
# ()
# >>> tuple(1,3,5)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: tuple expected at most 1 arguments, got 3
# >>> tuple((1,2,3))
# (1, 2, 3)
# >>> x = tuple((1,2,3))
# >>> x = (1,2,3)
# >>> x
# (1, 2, 3)
# >>> x = [1,2,3]
# >>> my_tuple = tuple(x)
# >>> my
# my_bool    my_list    my_name    my_set     my_string  my_tuple
# >>> my_tuple
# (1, 2, 3)
# >>> my_set2 =
# KeyboardInterrupt
# >>> my_tuple2 = (1,1,3)
# >>> my_set2 = set(my
# my_bool    my_list    my_name    my_set     my_string  my_tuple   my_tuple2
# >>> my_set2 = set(my_tuple2)
# >>> my_set2
# {1, 3}
# >>> my_dict = {"my_key": True}
# >>> my_dict["my_key"]
# True
# >>> my_dict
# {'my_key': True}
# >>> my_dict["my_key2"] = 2
# >>> my_dict
# {'my_key': True, 'my_key2': 2}
# >>> viddil = {"programming": ["Vasyl", "Oleg"], "new_viddil": ["Tetyana", "Dmytro"]}
# >>> viddil
# {'programming': ['Vasyl', 'Oleg'], 'new_viddil': ['Tetyana', 'Dmytro']}
# >>> viddil["programming"]
# ['Vasyl', 'Oleg']
# >>> viddil["new_viddil"]
# ['Tetyana', 'Dmytro']
# >>> viddil["new_viddil2"] = "Andriy"
# >>> viddil["new_viddil2"]
# 'Andriy'
# >>> viddil
# {'programming': ['Vasyl', 'Oleg'], 'new_viddil': ['Tetyana', 'Dmytro'], 'new_viddil2': 'Andriy'}
# >>> viddil["new_viddil"][0]
# 'Tetyana'
# >>> is_programmer
# False
# >>> viddil["is_proggramming"] = pr
# print(     property(
# >>> viddil["is_proggramming"] = is_programmer
# >>> viddil
# {'programming': ['Vasyl', 'Oleg'], 'new_viddil': ['Tetyana', 'Dmytro'], 'new_viddil2': 'Andriy', 'is_proggramming': False}
# >>> my_list = [1, 2, 3]
# >>> my_list[0]
# 1
# >>> set(1,2,3)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: set expected at most 1 arguments, got 3
# >>> set((1,2,3))
# {1, 2, 3}
# >>> {1,2,3}
# {1, 2, 3}
# >>> {1:1,2:2,3:3}
# {1: 1, 2: 2, 3: 3}
# >>> type({1:1,2:2,3:3})
# <class 'dict'>
# >>> try = 1
#   File "<stdin>", line 1
#     try = 1
#         ^
# SyntaxError: invalid syntax
# >>> in = 2
#   File "<stdin>", line 1
#     in = 2
#      ^
# SyntaxError: invalid syntax
# >>> a = 5
# >>> b = 2
# >>> a % b
# 1
# >>> a // b
# 2
# >>> a * b
# 10
# >>> a / b
# 2.5
# >>> a - b
# 3
# >>> a + b
# 7
# >>> 6 + 6
# 12
# >>> a == b
# False
# >>> c = 2
# >>> c == b
# True
# >>> c == a
# False
# >>> c != a
# True
# >>> c <> a
#   File "<stdin>", line 1
#     c <> a
#        ^
# SyntaxError: invalid syntax
# >>> c > a
# False
# >>> c < a
# True
# >>> c >= a
# False
# >>> c <= a
# True
# >>> d = 4
# >>> d += a
# >>> d
# 9
# >>> d = d + a
# >>> d
# 14
# >>> f = 7
# >>> d /= f
# >>> d
# 2.0
# >>> d **= f
# >>> d
# 128.0
# >>> d *= f
# >>> d
# 896.0
# >>> d //= f
# >>> d
# 128.0
# >>> input("Mesage: ")
# Mesage: 2
# '2'
# >>> user_input = input()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyboardInterrupt
# >>> user_input = input("Please input value")
# Please input value2
# >>> user_input
# '2'
# >>> user_input + 2
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: can only concatenate str (not "int") to str
# >>> user_input = int(user_input)
# >>> user_input
# 2
# >>> user_input + 2
# 4
# >>> user_input
# 2
# >>> user_input = user_input + 2
# >>> user_input
# 4
# >>> user_input += 2
# >>> user_input
# 6
# >>> print("1")
# 1
# >>> 1
# 1
# >>> print(user_input)
# 6
# >>> print("hello %s", user_input)
# hello %s 6
# >>> print("hello", user_input)
# hello 6
# >>> print("hello", user_input, user_input)
# hello 6 6
# >>> print("hello")
# KeyboardInterrupt
# >>> to_print = "{user_input}"
# >>> print()
# KeyboardInterrupt
# >>> to_print = "our number is: {user_input}"
# >>> to_print = "{user_input"
# KeyboardInterrupt
# >>> print(to_print)
# our number is: {user_input}
# >>>
