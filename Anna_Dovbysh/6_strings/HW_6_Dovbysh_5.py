def valid_phone_number(my_ph_numb):
        if len(my_ph_numb) == 13 and my_ph_numb [0:4] == '+380':
            print('valid')
        else: print('not valid')

#my_ph_numb = '+380977134900'
#valid_phone_number(my_ph_numb)