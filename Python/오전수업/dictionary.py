
# 딕셔너리 - 사전
# 파이썬 딕셔너리, 자바에서는 Map
# key : value

dic = { 
  '이름' : '이순신',
  '나이' : 24,
  '직업' : '군인'
}

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


title = ["이름", "키", "몸무게", "관심분야"]

# 5명의 정보를 입력한다.

info = []
for i in range(5):
  data = []
  for t in title:
    data.append(input(t + " : "))
  info.append(data)

# 이름을 키로 사용하여 딕셔너리에 5명의 정보를 저장하시오

# print(info)

member = dict()

for i in info:
  member[i[0]] = i

print(member)