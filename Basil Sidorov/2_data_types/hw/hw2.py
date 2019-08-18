price = 5000
price += 10

print("choose brand?")
brand = input()
price +=10
print("Choose model?")
price +=10
model = input()
print("choose Color?")
color = input()
price +=10
print("choose year?")
year = int(input())
price +=10
print("choose engine volume?")
engine_volume = int(input())
price +=10
print("choose odometer?")
odometer = int(input())
price +=10
print("enter phone number")
phone_number = input()
price +=10

result = price * 10 / 100
print(result)

odometer -= 50

year -= 2

print(f"""Your car will be {brand} brand, {model} model,
      in {color} Color, made in {year} year,
      engine has a {engine_volume} L volume,
      with {odometer} odometer, and we will call you via this number {phone_number}""")
