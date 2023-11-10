import requests
import time
from bs4 import BeautifulSoup


url = 'https://www.baidu.com'
res = requests.get(url).text
content = BeautifulSoup(res,"html.parser")
data = content.find_all('div',attrs={"id": {'lg'}})
print(data)
picture_list = []
for d in data:
  plist = d.find('img')['src']
  picture_list.append(plist)
print(picture_list)