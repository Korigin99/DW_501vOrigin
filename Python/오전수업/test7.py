import random

# 각 도시의 신생아, 초등학생, 중학생, 고등학생, 대학생, 노년층의 인구 수를 입력하시오
# 딕셔너리에 저장하시오
# 어떤 것이 키이고 어떤 것이 value로 들어가야할지 생각해보기

city = ("서울" , "대전", "대구", "광주", "부산", "울산", "세종")
kind = ("신생아", "초등학생", "중학생", "고등학생", "대학생")

# 답안

population = dict()
for cname in city:
  temp = dict()
  print("==== {0} 지역 인구수 ====".format(cname))
  for k in kind:
    i = random.randint(1000,50000)
    print("{0} : {1}명".format(k,i))
    temp[k] = i
    # 키 - 신생아, 초딩, 중딩 .... : value - 인구수
  population[cname] = temp

for k in population:
  print("{0} : {1}".format(k,population[k]))

""" l = []
res = dict()

for i in range(7):
  list1 = list()
  for j in info:
    list1.append(input(city[i]+"의 "+j+" : "))
  l.append(list1)

for i in range(len(city)):  
  res[city[i]] = dict(zip(info,l[i]))

print(res) """