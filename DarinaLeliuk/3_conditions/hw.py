#homework-1
# * Use input for get:* Brand * Model* Color * Year* Engine volume* Odometer* Phone number
inputbrand=input("Would you be so kind to tell a brand?")
inputmodel=input("Would you be so kind to tell a model?")
inputcolor=input("Would you be so kind to tell a color?")
inputyear=input("Would you be so kind to tell a year?")
inputev=input("Would you be so kind to tell an engine volume?")
inputodometer=input("Would you be so kind to tell a odometer?")
inputphn=input("Would you be so kind to tell a phone number?")
#* Create rating value for car and increase or decrease at each step
carscore=0
if inputbrand is "Audi" :
    carscore +=20
else: carscore +=10
if inputmodel is "A9":
    carscore +=30
else: carscore +=10
if inputcolor is "red":
    carscore +=20
else: carscore +=10
if int(inputyear) is 2019:
    carscore +=40
else :
    if int(inputyear) is 2018:
        carscore +=20
    else:
        carscore +=5
if float(inputev) is 4.2:
    carscore +=10
else:
    carscore +=5
if int(inputodometer)<1000:
    carscore +=20
else:
    if int(inputodometer)<50000:
        carscore +=15
    else:
        if int(inputodometer)<100000:
            carscore +=10
        else:
            carscore +=5

#* Check that brand (model, color) not in your favourite, print brand name,  and in finally clause print your favourite.
#* Try to change year type to int and catch exception, else print year  and finally decrease year by 1 and print
try:
    int(inputyear)
except ValueError as e:
    print ('Invalid input')
new_year=int(inputyear)-1
print(new_year)
# * Change Engine volume type to float and add 0.1 to value  (print to user), (use try, except, else)
# * Change odometer type to int check that odometer value less than 1000, greater than 50000, greater or equal to 100000 and
# set different value for rating

#* Get final rating for your car by your criterion (3-4 if cases)
print (f"Your final score is {carscore}")


#homework-2
#* Input: credit card number (fake data), cvv, mm/yy
cc=input("Would you be so kind to tell a cc number?")
cvv=input("put cvv here")
ym=input("enter mm/yy")
#* Check that credit card number length has 16 symbols in other case call exit()
#* Try to make credit card number to int() if error output "OK", in other case call exit()
try:
    len(int(cc)) is not 16
except ValueError as err:
    print("not valid value")

else:
    try:
        len(int(cvv))<3
    except ValueError as er:
        print("not valid value")
        GeneratorExit
    else: print("Everything fine")
finally:
    print("Length ok")

#* Check length of cvv if less than 3 symbols, print error and call exit()
#* If all checks passed print "Everything fine"