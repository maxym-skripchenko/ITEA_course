import re


string = 'asdf fjdk;afed,fjek,asdf,foo'
a = re.findall('\w+', string)
print(a)

li = ["+380971236789", "+380809123232", "99999x9999"]
for i in li:

    match = re.fullmatch('[+]380\d{9}',i)
    if match:
        print(f'{match.group()} and {i}')


emails = ['ssss@gamil.com', 'kjskjkw@mail.ru','jdjdd@yandex.ru']
domains = []
pattern = re.compile('[a-z]+[.][a-z]+')

for i in emails:

    domains.append(pattern.search(i).group())

print(domains)
