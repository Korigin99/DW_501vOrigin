# 문제 1.
# 시속 vk/h로 달리고 있는 자동차가 반지름 rkm인 원형 트랙을 달리고 있다면
# 한 바퀴 완주하는데 걸리는 시간은 몇 분인가?

# 원의 둘레 : 파이r


""" v = float(input("자동차의 속도를 입력하세요 : "))
r  = float(input("원형트랙의 반지름을 입력하세요 : "))

r = r * 2 * 3.14

time = r / v * 60

print("한 바퀴 완주 하는데 걸리는 시간 => {0:.1f}  분" .format((time))) """


# 문제 2
# 소주 한잔에 수명이 2분 단축된다.

""" x = int(input("하루에 소주를 몇 잔 마시나요 : "))

time = 2 * 365 * 20

life = x * time
print("수명이 {0} 분 줄었다".format(life))
print("수명이 {0} 시간 줄었다".format(life / 60))
print("수명이 {0} 일 줄었다".format(life / 60 / 24)) """

""" x, y, z = "a", "b", "c"
a = b = c = "f"
favorite = ['a', 'b', 'c']
a, b, c = favorite
print(a)
print(b)
print(c)
 """

""" 
  같다 -> ==, 같지 않다 -> != , > < >= <=
 """

""" num = 19
num1 = 27

if num1 > num:
    print("누난 내 여자니까!")
else:
    print("헤응")

age = 22

if age > num :
  print("내가 형이야")
elif age == num:
  print("우린 동갑이야~")
else:
  print("내가 더 많아~")

name = "hg"

print("미안") if name == "hg" else print("stop") """


# 문제 3

""" b = int(input("1. 펀치 점수 : "))
g = int(input("2. 펀치 점수 : "))

if b > g:
  print("기원 승")
else : 
  print("지연 승") """


# 문제 4

# 영주하고 지연이하고 수정이가 시험을 봤다 세 명의 시험점수를 입력하고 세명의 등급이 어떻게 되는지 출력하기
# 90점 이상 a

""" score = int(input("세명의 점수를 입력하세요"))

score = (score.split(" ")[0] + score.split(" ")[1] + score.split(" ")[2]) /3


if score >= 90:
  print("A")
elif score >= 80:
  print("B")
elif score >= 70:
  print("C")
else:
  print("쯧쯧") """


""" i = 1
while i<=10:
  print(i)
  i += 1 """

""" x = 1
while x<10:
  print(x * 4)
  x+=1 """


""" i = 1
while i < 5 :
  print(i)
  i += 1
else : 
  print("5보다 크면 반복문 종료 돼")
 """
""" i = 1
while True:
  print(i)
  if i==100: break
  i +=1 """


# while문 마지막 문제
# 배꼽 지연이가 버스를 타려고 교통카드를 만원 충전하였다
# 지연이가 버스를 몇번 탈 수 있는가? 잔액은 얼마인가?
# 버스요금은 1200원

""" card = 10000
cnt = 0

while card >= 1200:
  card -= 1200
  cnt += 1
else:
  print("버스를 탄 횟 수 {0}, 남은 잔액 {1}".format(cnt, card)) """

""" for i in range(10):
  print(i)

for i in range(1,10):
  print(i*8) """
 
for i in range(45,110):
  print(i)

