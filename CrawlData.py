import requests
from bs4 import BeautifulSoup
import re

link_page = "https://zingnews.vn"
urlBing = f"https://www.bing.com/search?q={link_page}"
urlBing_get = requests.get(urlBing)
soup_urlBing = BeautifulSoup(urlBing_get.text, 'html.parser')
containers_urlBing = soup_urlBing.find_all('li', {'class': 'b_no'})
for a in containers_urlBing:
    get_urlBing = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', a.h1.text)
    convert_urlBing = "".join(get_urlBing)
    request_convert_urlBing = requests.get(convert_urlBing)
    soup_request = BeautifulSoup(request_convert_urlBing.text, 'html.parser')
    containers_request = soup_request.find_all('img', alt=True)
    for container_request in containers_request:
        if container_request.has_attr('data-src'):
            dataSrc = container_request['data-src']
            dataAlt = container_request['alt']
            removechar_special = re.sub("[@_!#$%^&*()<>?/\|}{~:']", '', dataAlt)

            response = requests.get(dataSrc)
            print("Processcing_datasrc ....... " + '\n' + dataSrc)

            file = open(removechar_special + '.png', "wb")
            file.write(response.content)
            file.close()
        elif container_request.has_attr('src'):
            dataSrc_Src = container_request['src']
            dataAlt = container_request['alt']
            removechar_special = re.sub("[@_!#$%^&*()<>?/\|}{~:']", '', dataAlt)

            response = requests.get(dataSrc_Src)
            print("Processcing_src ....... " + '\n' + dataSrc_Src)

            file = open(removechar_special + '.png', "wb")
            file.write(response.content)
            file.close()


# page = requests.get("https://zingnews.vn")
# soup = BeautifulSoup(page.text, 'html.parser')
# containers = soup.find_all('img', alt=True)
# container_video = soup.find_all('')
# for container in containers:
#     if container.has_attr('data-src'):
#         dataSrc = container['data-src']
#         dataAlt = container['alt']
#         removechar_special = re.sub("[@_!#$%^&*()<>?/\|}{~:']", '', dataAlt)
#
#         filename = dataSrc.split('/')[-1]
#         response = requests.get(dataSrc)
#
#         print("Processcing ....... " + '\n' + dataSrc )
#
#         file = open(removechar_special + '.png', "wb")
#         file.write(response.content)
#         file.close()
