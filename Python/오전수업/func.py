# 함수
# 자바의 메서드
# 바환타입 메서드이름(매개변수) { 매서드 실행내용; 반환타입있다면 return;}
# 자바스크립트 함수
# function 함수이름(매개변수){함수실행내용; 반환값 있다면 return;}

# 파이썬 함수
# def 함수이름(매개변수): 

# 정의된 함수 실행방법 -> 함수이름()
""" 
def sum(x, y):
  return x+y

res = sum(10,20)
print(res)

def func():
  print("나 함수다")

func()

def func1(word):
  print(word+" 이다")

func1("난 바보")

def minus(num1, num2):
  print(num1 - num2)

minus(30, 15)

def whoami(name, what):
  if name == "김기원":
    print(name + "는(은) " +what + "이다.")

whoami("김기원", "프로그래머")

def count(i):
  return i+1

cnt=0
while cnt<10:
  cnt = count(cnt)

print(cnt)

cnt1=0

def count2():
  global cnt1 # 파이썬의 전역변수 - count2 함수에서 cnt1을 사용하고자 한다면 global 붙여서
              # 전역 변수임을 알려주고 사용한다.
              # 전역변수는 최소함으로만 사용 - 코드의 유지보수를 어렵게 한다.
              # 전역변수를 마구 생성하여 사용하면 정신적인 대미지를 입는다.
  cnt1 += 1


while cnt1<10:
  count2()
print(cnt1) 
"""

""" def add(x):
  print(x+100)

num = int(input("정수 입력 : "))
add(num) """

# 첫 번째 할 것. 정수 두개 입력받기
# 두 번째 할 것. 정수 입력받는 코드 위에 함수 만들기
# 함수의 내용은 두숫자를 곱해서 출력하는 내용
# 세번째 할 것 정수 입력받는 코드 밑에 함수 호출하기

""" def mul(x,y):
  print(x*y)

x = int(input("첫번째 정수 입력 : "))
y = int(input("두번째 정수 입력 : "))

mul(x,y) """

""" def add1(x):
  for i in x:
    print(i + 1)

list1 = [i for i in range(2, 50, 2)]
add1(list1) """
""" 
def score_input(s):
  scr = []
  for sub in range(len(s)):
    scr.append(int(input(s[sub] + " : ")))
  return scr

def total(src):
  sum = 0
  for i in src:
    sum += i
  return sum

def avg(t):
  t = t/3
  return t



score = []
subj = ("국어 점수", "영어 점수", "물리 치료")

score = score_input(subj)
tot = total(score)
avg = avg(tot)
 """


""" def tall_input(l):
  li = []
  for i in range(len(l)):
    li.append(int(input(l[i] + ":")))
  return li

def tall_avg(l):
  avg = 0
  for i in l:
    avg += i
  avg = avg / len(l)
  return avg

def small(li,li2, avg):
  for i in range(len(li)):
    if li2[i] < avg:
      print("평균 키보다 작은 사람 : " + li[i])


li = ["장영순", "김지언", "이지형"]
li2 = tall_input(li)
avg = tall_avg(li2)
small(li,li2,avg) """

""" def find(li):
  for i in li:
    if i % 5 == 0:
      print("5의 배수 : {0}".format(i))

li = [i for i in range(5,51)]

find(li) """



# =====================

""" def func1(national="계림국"):
  print(national)

func1("대한민국")
func1() """


#======================

""" def func2( **info):
  print(info["name"])
  print(info["상태"])

func2(name="장영주", 상태="천재 아름다움") """

#========================

# 첫번째 리스트에는 이순신, 장영실, 정몽주, 정도전, 이성계, 이방지 의 키를 입력
# 두번째 리스트에는 이순신, 장영실, 정몽주, 정도전, 이성계, 이방지의 몸무게를 입력

def small(name, hei):
  min = hei[0]
  n = name[0]
  for i in range(len(hei)):
    if hei[i] < min:
      min = hei[i]
      n = name[i]
  print("키가 제일 작은 사람 : {0}".format(n) )

def fat(name, wei):
  min = wei[0]
  n = name[0]
  for i in range(len(wei)):
    if wei[i] > min:
      min = wei[i]
      n = name[i]
  print("몸무게가 가장 많이 나가는 사람 : {0}".format(n) )

name = ["이순신", "장영실", "정몽주", "정도전", "이성계"]

hei = []
wei = []

for i in name:
  hei.append(int(input(i + "의 키 : ")))
  wei.append(int(input(i + "의 몸무게 : ")))

small(name, hei)
fat(name, wei)


 

