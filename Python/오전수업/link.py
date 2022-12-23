import bs4
import requests

def getHref(html_tag):
  mul = bsp.find("ul",{"class","permanent-list-body"})
  href_list = []

  ali = mul.findAll("li")
  for a in ali:
    sul = a.findAll("ul",{"class", "permanent-area"})
    for li1 in sul:
      li = li1.findAll("li")
      for li_1 in li:
        if li_1.find("a"):
          href_list.append(li_1.find("a")["href"])
  return href_list


url = "https://www.museum.go.kr/site/main/content/permanent_exhibition_guide"
site = "https://www.museum.go.kr"
result = requests.get(url=url)

bsp = bs4.BeautifulSoup(result.content, "html.parser")

href_list = getHref(bsp)

dic_column = ["title","menu"]

site_info = dict()

for href in href_list:
  link = site + href
  result2 = requests.get(url=link)
  sub_bsp = bs4.BeautifulSoup(result2.content,"html.parser")
  ptitle = sub_bsp.find("h2",{"class","page-title"}).text
  showtitle = sub_bsp.find("p",{"class","showroom-title"}).text
  ul = sub_bsp.find("ul",{"class","swiper-wrapper"})
  li = ul.findAll("li")
  menu = [l.find("a").text.strip() for l in li]
  site_info[ptitle] = dict(zip(dic_column,[showtitle, menu]))
  # print(ptitle, showtitle)

print(site_info)
  


""" a = bsp.findAll("a",{"class","permanent-img"})

href_list = []

for href in a:
  href_list.append(href.attrs['href'])

print(href_list) """

""" href_list = []
main_li = main_ul.findAll("li",{"class","e1oznup73"})
for li in main_li:
  sub_ul = li.find("ul")
  sub_li = sub_ul.findAll("li")
  for sli in sub_li:
    href_list.append(sli.find("a")['href']) """


# print(href_list)

