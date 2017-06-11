#!/usr/bin/env python3
import re
import sys
from bs4 import BeautifulSoup

import requests

url = input("Enter a website to extract the URL's from: ")

r  = requests.get("http://" +url)

data = r.text

soup = BeautifulSoup(data)

sys.stdout = open('file', 'a')
for link in soup.find_all('a'):
    print(link.get('href'))


# with open('file.csv', 'wb') as csvfile:
#     cwriter = csv.writer(csvfile, delimiter=' ',
#                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     for var in list_of_values:
#         cwriter.writerow(var)