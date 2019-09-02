'''Define a function that computes the length of a given list or string.
(It is true that Python has the len() function built in, but writing it
yourself is nevertheless a good exercise.)'''

def my_len(something):
    char_count = 0
    for element in something:
        if element:
            char_count += 1
    print(char_count)
