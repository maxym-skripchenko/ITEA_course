import re

abc = 'abc@gmail.com, abc@bigmir.net, abc@ukrtele.com'
emails = re.findall(r'@[\w\.-]+', abc)
for email in emails:
    print(email)