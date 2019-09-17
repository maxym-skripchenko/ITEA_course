class Card:
    def __init__(self, number=None, cvv=None, mm_yy=None):

        self.number = number
        self.cvv = cvv
        self.mm_yy = mm_yy

    def __str__(self):

        return f'Date = {self.mm_yy},cvv =  {self.cvv}, number = {self.number}'

a = Card()
a.number = input("number: ")
a.cvv = input('cvv: ')
a.mm_yy = input('date(mm/yy): ')
if len(a.number)!=16:
    exit(1)
try:
    a.number = int(a.number)
except:
    exit(1)
else:
    print('ok')
assert len(a.cvv) == 3, print('error')
print('everything is fine')