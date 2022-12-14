
# 딕셔너리 - 사전
# 파이썬 딕셔너리, 자바에서는 Map
# key : value
""" 
dic = { 
  '이름' : '이순신',
  '나이' : 24,
  '직업' : '군인'
} """

""" print(dic)
print(dic['이름'])

# 키로 사용가능 - 문자열, 정수, 실수, boolean
# 키 사용 불가 - 리스트, set, 딕셔너리
# value 사용 - 아무거나 다

dic = {} # 이거는 set 아니고 딕셔너리로 인식
dic = dict() # 딕셔너리 생성

dic1 = dict(이름='김기원', 나이=24, 직업='개발자')
print(dic1)

dic2= dict([('이름','김기투'),('age',24),('특징', '알면서')])
print(dic2)

dic3 = dict(zip(['이름','나이','관심분야'],['김기원',24,'game']))
print(dic3)
  
print(dic3['이름'])
dic3['관심분야'] = '게임'
print(dic3)

dic3['싫어하는것'] = '굴'
print(dic3) """

# if '이름' in dic3:
#   print("너의 이름은 : {0}".format(dic['이름']))
# else:
#   print("존재하지 않는 키 입니다.")

# 딕셔너리 키 몇개?
# print(len(dic3))
""" 
title = ["캐릭터명", "생명력", "코딩기술", "잔머리", "수학능력", "공간능력", "지능지수"]
data = []
for x in title:
  data.append(input(x + " : "))

# print(data)

info = dict(zip(title,data))
print(info)

for x in info:
  print(x) # 딕셔너리의 키 출력

for x in info:
  print(info[x]) # 딕셔너리의 value 출력

for x in info.values():
  print(x) # 딕셔너리의 value 출력

for key in info.keys():
  print(key) # 딕셔너리의 key 출력

for k, v in info.items():
  print(k, v) # output key, value of dictionary """


# title = ["이름", "키", "몸무게", "관심분야"]

# 5명의 정보를 입력한다.

""" info = []
for i in range(5):
  data = []
  for t in title:
    data.append(input(t + " : "))
  info.append(data) """

# 이름을 키로 사용하여 딕셔너리에 5명의 정보를 저장하시오

# print(info)

""" member = dict()

for i in info:
  member[i[0]] = i

print(member) """

#이름, 번호, c언어 성적, java성적, react 성적, db성적, 지적수준
# 10명의 성적을 딕셔너리에 저장하시오

# info = ['이름', '번호', 'c언어', 'java', 'react', 'DB', '지적수준']

""" st = []

for j in range(10):
  data = []
  for i in info:
    data.append(input(i + " : "))
    # print(data)
  student = dict(zip(info,data))
  st.append(student)
print(st)
 """

""" values = list()
for i in range(2):
  temp = list() # 입력한 값이 저장될 리스트
  for k in info:
    temp.append(input(k))
  values.append(temp)

class501 = dict()
for v in values:
  class501[v[0]] = dict(zip(info,v))

for k in class501:
  print("{0} : {1}".format(k, class501[k]))

avg = list()
dic_avg = dict()
for name in class501: # name에는 키로 사용한 이름이 저장
  sum = 0
  title = list(class501[name].keys()) # 딕셔너리의 키를 리스트로 변환
  for i in range(2,6):
    sum = sum + int(class501[name][title[i]])
  # for title in class501[name]: # title에는 이름, 번호, 성적들
  #   if title=="이름" or title=="번호" or title == "지적수준":
  #     continue
  #   sum = sum + int(class501[name][title]) # 한 명의 성적 종합 구하기
  
  dic_avg[name] = dict(평균점수=sum/4, 지적수준=class501[name]['지적수준'])

print(dic_avg) """

# 딕셔너리의 key만 리스트로 변환
# li = list(dic.keys())
# 딕셔너리의 value만 리슴트로 변환
# li = list(dic.values())
# 딕셔너리의 key, value를 리스트로 변환
# li = list(dic.items())
# key와 value를 한 쌍으로 튜플 형태로 저장
# [('k1' : 'v1'), ('k2' : 'v2')]

""" res = dict()
list2 = list()

title2 = ['평균', '지적수준']

for i in class501:
  temp1 = class501[i]
  list1 = list()
  list3 = list()
  dic2 = dict()
  for j in temp1:
    list1.append(temp1[j])
  avg = (int(list1[2]) + int(list1[3]) + int(list1[4]) + int(list1[5]))/4
  k = list1[6]
  list3.append(str(avg))
  list3.append(k)
  for d in list3:
    dic2 = dict(zip(title2,d))
  list2.append(dic2)

for i in class501:
  res = dict(zip(i,list2))

print(res) """

# 문의제목, 작성자, 문의내용, 작성일, 답변, 답변일
# 딕셔너리에 저장하는데 키는 번호를 사용, 파일에서 읽어드린 순서대로 1번부터 부여

file=[]
with open("c:/test/question.txt","r",encoding="utf-8") as f:
  file=f.readlines()

title = ["문의제목", "작성자", "문의내용", "작성일", "답변", "답변일"]

dic1 = dict()
for i in range(len(file)):
  file[i] = file[i][:len(file[i])-1]
  file[i] = file[i].split(" ")

for i in range(len(file)):
  dic1[i+1] = dict(zip(title,file[i]))

# for i in dic1:
  # print("{0} : {1}".format(i,dic1[i]))

for num in dic1:
  print("{0}. {1} {2}".format(num,dic1[num]["문의제목"],dic1[num]["작성일"]))

search = int(input("문의 번호를 입력하세요 : "))


print("작성자 : " + dic1[search]['작성자'])
print("제목 : " + dic1[search]['문의제목'])
print("작성일 : " + dic1[search]['작성일'])
print("문의글 : " + dic1[search]['문의내용'])
print("==========================")
print("답변 : " + dic1[search]['답변'])
print("답변일 : " + dic1[search]['답변일'])
