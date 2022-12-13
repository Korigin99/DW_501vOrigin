import random

""" name = ["김유신", "이순신", "어영담", "이성계", "장영실", "홍길동", "김지연", "김춘추"]
job = ["군인", "국회의원", "과학자", "도둑", "건설업자", "밸리댄서", "변호사"]
age = [24, 35, 37, 21, 54, 41, 29, 35, 42]

info = []

for i in range(8):
    info.append([random.choice(name), random.choice(job), random.choice(age)])

print(info)


avgAge = 0
cnt = 0
for i in info:
    if "군인" == i[1]:
        print("직업이 군인인 사람의 이름 : " + i[0])
    if "과학자" == i[1]:
        avgAge = avgAge + int(i[2])
        cnt += 1
    if int(i[2]) < 30:
        print("나이가 20대인 사람의 직업 : " + i[1])
if cnt != 0:
  print("직업이 과학자인 사람들의 평균 나이 : " + str(avgAge/cnt))
else :
  print("과학자가 없다.") """
"""

# 랜덤 사용 방법
# random.randint(1,40) -> 1~40 중에서 랜덤

a = [] # 랜덤 범위 1~30
b = [] # 랜덤범위 10~50
c = [] # 랜덤 범위 1 ~ 100

num=[]
# a, b, c 리스트에 각각 15개씩 랜덤 범위에 맞춰서 저장하기
# a,b,c 리스트의 값 중에서 중복인 값만 찾아서 num 리스트에 저장하기

for i in range(15):
  a.append(random.randint(1,30))
  b.append(random.randint(10,50))
  c.append(random.randint(1,100))


for x in a:
  if x in b:
    if x in c:
      num.append(x)


if not num:
  print("없어")
else : 
  print(num)
"""

word = ["boy", "table", "book", "girl", "interest", "limit", "endless", "mission", 
      "hopi", "tigerprint"]

eng = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", 
      "s", "t", "u", "v", "w", "x", "y", "z"]

# eng 리스트의 알파벳을 무작위 조합해서 word 리스트의 단어 중 1개이상 나오는경우
# 몇 번째 조합에서 나오는지 출력

res = ""
cnt = 0
while (True):
  cnt += 1
  l = random.randint(3, 10)
  for i in range(l):
    res += random.choice(eng)
  if res in word:
    break
  res = ""

print(res + "가 생성되기 까지의 횟수 : " + str(cnt))


