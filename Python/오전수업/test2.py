import random

""" num = random.randint(1,3)

print(num)

firstname = ["김", "장", "이", "최", "윤", "변"]
middle = ["기", "지", "영", "윤", "재", "종"]
last = ["원","연","현","연","도"]

a = random.choice(firstname)
b = random.choice(middle)
c = random.choice(last)
print(a+b+c) """

info = [ 
  ["김기원", "콘샐러드", "시험"], ["이지현", "나이", "민감"], ["김지연", "배꼽", "선생님배꼽찔러봄"], ["장영주", "후크선장", "공통점"],
  ["윤재영","비니","강균성"], ["리정수", "군대", "인민군"]
]

""" for i in info:
  for k in i:
    print(k) """

""" q = input("이름 또는 특징 입력 : ")

for i in info:
  for k in i:
    if q in k:
      print(k) """

""" info = [ 
  ["김기원", "콘샐러드", 13], ["이지현", "나이", 33], ["김지연", "배꼽", 34], ["장영주", "후크선장", 13],
  ["윤재영","비니",33], ["리정수", "군대", 32]
]
for i in info:
  if i[2]>=30 and i[2]<=39:
    print(i) """


""" age = [0,0,0,0,0,0]
age30 = []
연장자 = ""
max = 0

for 개인 in info:
  age[int(개인[2]/10)] += 1
  if 개인[2]>=30 and 개인[2]<40:
    age30.append(개인[1])
    if max < 개인[2]: """
      

