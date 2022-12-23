import bs4
import requests
from urllib.request import urlopen

url = "https://www.graychic.co.kr/product/list.html?cate_no=4"
#res = requests.get(url=url)
html = urlopen(url)

bsp = bs4.BeautifulSoup(html, "html.parser")

href_list = []
items = bsp.findAll("div",{"class","sp-product__thumb"})
for item in items:
  href_list.append(item.find("a")['href'])

site = "https://www.graychic.co.kr"

# print(href_list)

# item = bsp.findAll("div",{"class","info"})
# for i in item:
#   print("제품 : {0}, 가격 : {1} ".format(i.find("p",{"class","name"}).text, i.find("span",{"class","p_value"}).text))

""" names = bsp.findAll("p",{"class","name"})
price = bsp.findAll("span",{"class","p_value"})


item = []

for i in range(len(names)):
  name = names[i].find("a").text
  p = price[i].find("strong").text
  item.append([name, p])

print(item) """

