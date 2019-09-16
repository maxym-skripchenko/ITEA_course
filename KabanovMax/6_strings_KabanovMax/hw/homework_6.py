import re

mail = 'user@gmail.com, user@bigmir.net, user@icloud.com'

emails = re.findall(r'@[\w\.-]+', mail)

for email in emails:
    print(email)