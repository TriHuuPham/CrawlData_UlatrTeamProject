import requests
from bs4 import BeautifulSoup
import os
import re


page = requests.get("https://zingnews.vn")
soup = BeautifulSoup(page.text, 'html.parser')
containers = soup.find_all('img', alt=True)
for container in containers:
    if container.has_attr('data-src'):
        dataSrc = container['data-src']
        dataAlt = container['alt']
        # print(dataSrc)
        # print(dataAlt)
        removechar_special = re.sub("[@_!#$%^&*()<>?/\|}{~:']", '', dataAlt)

        filename = dataSrc.split('/')[-1]
        response = requests.get(dataSrc)

        print("Processcing ....... " + '\n' + dataSrc )

        file = open(removechar_special + '.png', "wb")
        file.write(response.content)
        file.close()
