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

""" for i in range(45,110):
  print(i) """


""" for i in range(1, 101):
    if i % 3 == 0:
        print("윤재영", end="")
    if i % 5 == 0:
        print("바보") """

""" name = ["장영주", "김지연", "윤재영"]
print(name)
data = ["김기원", 100, 3.14, True]
print(data)

data2 = list(("최윤도", "변수정", 100))
print(data2)

print(data2[0])
print(data[-1])

data3 = ["이종빈", "윤종찬", "이지현", "장영주"]
print(data3[1:3])
print(data3[:3])
print(data3[:])
print(data3[2:])

data3.append("김지연")
data3.append("윤재영")
print(data3)

data3.remove("장영주")
print(data3)
data3.pop()
print(data3)

del data3[2]
print(data3)

data3.clear()
print(data3) """

""" memo = ["나", "너", "우리", "우리들"]
for me in memo:
  print(me , end="")

print()
memo[3] = "껄껄"
for me in memo:
  print(me, end="")

memo[1:4] = ["장영주","는","밥을"]
print()
for me in memo:
  print(me,end="")

memo.insert(3, "드러운 어그와")
print(memo)

memo1 = ["이종빈", "윤재영", "변수정"]
memo2 = ["장영주", "김지연", "이지현"]
memo1.extend(memo2)
print(memo1)

print(len(memo1)) """


# list 생성
# 1. memo = ["a", "b", "c"]
# 2. memo = list(("a","b","c"))
# 데이터 추가 memo.append("abc")
# 데이터 삽입 memo.insert(2, "abc")
# 데이터 삭제
# 삭제 데이터 지정 memo,remove("c")
# 마지막 데이터 삭제 memo.pop()
# 인덱스로 삭제 del memo[3]
# 배열 합치기 memo.extend(리스트 이름)
# 리스트 크기 len(리스트 이름)
# 갯수 구하기 memo.count("a") - a 라는 데이터의 개수를 찾을 떄 사용
# 인덱스 찾기 memo.index("a") - a 라는 데이터는 몇번 인덱스에 있는지 찾을 때 사용
# 정렬 memo.sort() - 오름차순, memo.sort(reverse=True) - 내림차순
# 반전 memo.reverse()


info501 = ["장영주는 폭력적이다", "김지연은 연하만 좋아한다", "윤재영은 옆 반 썜을 좋아한다",
           "최윤도는 영주불행이 행복이다", "수정이는 생일이라 코딩이 싫대...", "종빈이는 지금 게임한다."]

""" name = input("학생의 이름을 입력하세요 : ")

for i in info501:
    if name in i:
        print(i)
        break
else:
    print("입력하신 정보가 없습니다")

s = "" """

""" for i in info501:
  if "좋아한다" in i:
    print(i) """

num = [ x for x in range(10)]
print(num)