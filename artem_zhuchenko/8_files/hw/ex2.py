# Create program that get [Text](https://www.python.org/dev/peps/pep-0008/#code-lay-out)
# from file, find 5 most popular words and write result to file.

import urllib.request
from collections import Counter
from bs4 import BeautifulSoup

response_text = urllib.request.urlopen("https://www.python.org/dev/peps/pep-0008/#code-lay-out")
soup = BeautifulSoup(response_text.read(), from_encoding=response_text.headers.get_content_charset('charset'))

content = soup.text
split_text = content.split()

words_counter = Counter(split_text)
most_occur = words_counter.most_common(5)

print(most_occur)
data = dict(most_occur)
data = str(data)

with open("popular_words_from_urls_results.txt", "r+") as file:
    file.write(data)
