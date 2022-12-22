
# HTTP - 하이퍼텍스트(html) 을 전송하기위한 프로토콜
# 프로토콜 -  약속, 규약 
# url -  http://www.naver.com
# uri -   url 에    사용자 정보와 스키마 를 포함한값

# 스크래핑 - 웹페이지에서 자동으로 데이터를 추출하는것, 웹 페이지 소유자의 허락없이
          #  무단으로 끌어 오는행위
# 크롤링 -   웹페이지에서 자동으로 데이터 추출
#  스크래핑은 특정 웹사이트에서 데이터 추출,  크롤링은 웹사이트의 링크를통해서 정보
# 를 찾아서 추출하는 방식 
#  둘다  데이터 추출한다라는 것이 동일하기에  흔히 크롤링이라고 한다.


from urllib.request import urlopen
import bs4

# test_html = "<html><head></head><body><div>hahahaha</div>"
# test_html +=" <p>kjy babo</p> </body></html>"

# bobj = bs4.BeautifulSoup(test_html,"html.parser")

# print(test_html)
# print( bobj)

# print( test_html.find("div"))
# print( bobj.find("div"))
# print(bobj.find("p"))

#url="https://www.naver.com"
#html = urlopen(url)

#print(html.read())

# html ="""
# <html>
#     <body>
#         <div>
#             <ul class="kjy">
#                 <li>babo</li>
#                 <li>19</li>
#             </ul>
#             <ul class="ljh">
#                 <li>old mai...</li>
#                 <li>old...</li>
#             </ul>
#         </div>
#     </body>
# </html>
# """
# bsp = bs4.BeautifulSoup(html,"html.parser")

# # 태그의 속성을 통해서 가져오는 방법
# ul = bsp.find("ul",{"class":"ljh"})
# print(ul['class'])

# li = bsp.findAll("li")
# print( li[1] )

# for i in li:
#     print(i.text)



# url = "https://news.naver.com/main/list.naver?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y"
# html = urlopen(url)
# html = html.read()

# bsp = bs4.BeautifulSoup(html,"html.parser")

# news_ul = bsp.find("ul", {"class","type02"})
# news_li = news_ul.findAll("li")

# for li in news_li:
#     strong = li.find("strong")
#     print(strong.text)

""" url = "https://comic.naver.com/webtoon/weekday"
html = urlopen(url)
html = html.read()

bsp = bs4.BeautifulSoup(html,"html.parser") """
""" 
webtoon = bsp.find("div",{"class","col_selected"})

thu = webtoon.findAll("li")

for i in thu:
    week = i.find("a",{"class","title"})
    print(week.text)
 """
""" div = bsp.findAll("div",{"class","col_inner"})
ul = div[3].find("ul")
lis = ul.findAll("li")
for i in lis:
    a = i.find("a",{"class","title"})
    print(a.text) """


url = "https://ethereum.org/ko/"
html = urlopen(url)
html = html.read()

bsp = bs4.BeautifulSoup(html,"html.parser")


    