""" 
# set
# 리스트와 달리 순서, 중복 없이 사용
# 순서가 없다라는 말은 입력한 순서대로 저장 돼 있지 않는다.
# 중복 제거가 필요한 경우에 사용
# 그룹 구성할 떄 사용(집합)
# 데이터를 변경할 수 없지만 데이터를 제거하고 새 데이터 추가할 수 있다.
# set은 { } 로 작성된다.

# set 생성

set1 = {"사과", "배", "참외"}
print(set1)

set2 = set("member")
print(set2)

set3 = set("장역죽이가 죽을 먹었다. 근데 장영죽이가 죽을 먹다가 체했다.")
print(set3)

set4 = set(("장영실이","수도원옷을","잆었다"))
print(set4)

# print(set4[0]) 인덱스를 사용하여 set 데이터 접근 불가

for s in set4:
  print(s)

print("장영주가" in set4) # set 내부에 지정데이터가 있는지 확인

set4.add("김진연은")
print(set4)

set5 = {"안경을 쓰고있다.", "그래서", "겨울에는 장님이 된다."}
set4.update(set5)
print(set4)

list1 = ["장영주는", "화가많다"]
set4.update(list1) # 리스트 뿐 아니라 튜플, 딕셔너리 도 가능
print(set4)

# set 데이터 삭제하기

set4.remove("그래서") # remove는 삭제 데이터가 없으면 오류 발생
print(set4)
set4.discard("장영주는") # discard는 삭제 데이터가 없으면 오류 no
print(set4)

a = set4.pop() # 마지막 데이터를 추출 삭제, 마지막 데이터를 추출하여 밖으로 빼고 set에서는 삭제

print(set4)
print(a)

set4.clear() # set을 비움
del set4 # set을 완전 삭제

# 집합

장영주팀 = {"김기원","김민서","김민정","최윤도","정다현","임성민","이지현","이종빈"}
김지연팀 = {"윤재영", "이정수", "운종찬", "변수정", "최윤도", "이지현", "전계림"}

a = 장영주팀 - 김지연팀 # 차집합
print(a)
b = 장영주팀 | 김지연팀 # 합집합
print(b)
c = 김지연팀 & 장영주팀 # 교집합
print(c)
d = 김지연팀 ^ 장영주팀 # 합집합에서 교집합 빼기
print(d)

a = 장영주팀.difference(김지연팀) # 차집합
# 장영주팀.difference_update(김지연팀) # 차집합 - 장영주팀의 데이터가 변경됨
b = 장영주팀.intersection(김지연팀) # 교집합
# 장영주팀.instersection_update(김지연팀) # 교집합 - 장영주팀의 데이터가 변경됨
c = 장영주팀.symmetric_difference(김지연팀) # 합집합
# 장영주팀.symmetric_difference_update(김지연팀) # 합집합 - 장영주팀의 데이터가 변경됨
"""


""" 이정수팀장 = {"김기원", "최윤도", "장영주", "이종빈", "정다현", "김유신", "한석봉", "윤재영"}
이지현팀장 = {"김지연", "윤재영", "윤종찬", "변수정", "김유신", "한석봉", "이순신"}

스파이 = 이정수팀장.intersection(이지현팀장)
print("스파이" + str(스파이))

# 차집합
충신 = 이정수팀장 - 이지현팀장 # 이정수팀장.difference(이지현팀장)
print("이정수팀 : {0}".format(충신))

전계림 = {"장영주", "운재영", "김지연", "이종빈"}

이지현팀만봄 = 이지현팀장 - 전계림 
이지현팀만봄 = 이지현팀만봄 - 이정수팀장
print("완전한 이지현 팀 : {0}".format(이지현팀만봄)) """


# 문제
# today Question 1

import random


""" set1 = set()
while len(set1)<=10:
  ran = random.randint(1,50)
  set1.add(ran)

print(set1) """



member = [["김춘추", "01012345678", "남"],["김지연", "01032455678", "남"],["이순신", "01098745678", "남"],["하지원", "01034565678", "여"],["전계림", "01013245678", "남"],
["전지현", "01032415678", "여"],["윤재순", "01080345678", "여"],["이지현", "01008345678", "여"],["이요원", "01009815678", "남"]]

""" print("======= 회원가입 =========")
name = input("이름 : ")
tel = input("전화번호 : ")
gender = input("성별 : ")

member.append([name, tel, gender])
print(member) """

# 문제 2. 회원가입을 하는데 이름이 중복되지 않게 회원가입 될 수 있도록 만들기

isCheck = True

""" 
while(isCheck):
  print("======= 회원가입 =========")
  name = input("이름 : ")
  for i in member:
    if name in i[0]:
      print("이름 중복")
    else:
      isCheck = False
  if isCheck:
    continue
  tel = input("전화번호 : ")
  gender = input("성별 : ")
  member.append([name, tel, gender])
print(member)
 """

names = []
for x in member:
  names.append(x[0])

tempSet = set(names)

print("======회원가입=======")
name = input("이름 : ")

# a = len(set)
# set.add(name)
# if a!=len(set):

setName = {name}

while setName.issubset(tempSet): # issubset() - 저장한 set안에 값이 포함되어 있냐?
  print("이름 중복")
  name = input("이름 : ")

# issuperset() 0 a.issuperset(b) b가 a에 모두 있냐?
# A가 B에 포함되어 있냐?
# A.issubset(B) 또는 B.issuperset(A)

tel = input("전화번호 : ")
gender = input("성별 : ")
member.append([name, tel, gender])
print(member)

  

