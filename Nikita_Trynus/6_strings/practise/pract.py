import re


def generate_n_chars(c,n):

    return c*n


def is_palindrome(st):

    if st[:len(st)//2] == st[len(st):len(st)//2:-1]:

        return True

    else:

        return False


# Never underestimate the heart of the champion

def overlapping(a,b):

    return True if set(a).intersection(set(b)) else False



# print(is_palindrome('radar'))
print(overlapping([1,2,3],[838,892,1]))
string = 'AV is largest Analytics community of India'
print(string.split()[0],string.split()[-1])

pattern_1 = re.compile('[a-zA-Z]{2}')
splt = string.split()
new_splt = []
for i in splt:

    new_splt.append(pattern_1.match(i).group())

print(new_splt)

string_1 = 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'
pattern_2 = re.compile('\d\d-\d\d-\d{4}')
print(pattern_2.findall(string_1))
