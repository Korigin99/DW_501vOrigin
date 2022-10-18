import  csv
import random

""" f = open('info.csv','r')
rdr = csv.reader(f)

for line in rdr:
  print(line)

f.close() """

# 회원 번호는 PK

fn = ['김','박','이','황','정','최','유','성','육','장','곽','한','노','조']
mn = ['지우','민준','서윤','서준','서연','민서','하윤','도윤','시우','서현','연우',
      '주원','예준','지민','지호','하은','지원','서진','지후','지안','하준','윤서','지유',
      '채원','준서','준우','채은','수정','주호','선우']
sex = ['남','여']
interest = ['개발자 도구', '교육', '그래픽 및 디자인', '뉴스', '도서', '사진 및 비디오', '소셜 네트워킹', '스포츠', '게임', '쇼핑']


f = open('info.csv', 'a', newline='')
wr = csv.writer(f)

for i in range(100):
  fnRan = random.choice(fn)
  mnRan = random.choice(mn)
  sexRan = random.choice(sex)
  yearRan = random.randrange(1980,2005)
  monthRan = random.randrange(1,13)
  dateRan = random.randrange(1,32)
  interestRan = random.choice(interest)
  name = fn[fnRan] + mn[mnRan]
  dateBirth = str(yearRan)+"."+str(monthRan)+"."+str(dateRan)
  wr.writerow([i+1,name,sex[sexRan],dateBirth, interest[interestRan]])

f.close()


""" with open("info.csv", 'a') as f:
  f.truncate(0) """

