def overlapping(string_1,string_2):
    for element in string_1:
        if element in string_2:
           return True
    return False

#overlapping(['ua'],['awed'])