def find_longest_word(my_string):
    return max(len(word) for word in my_string.split())

#my_string = 'AV is largest Analytics community of India'
#print(find_longest_word(my_string))