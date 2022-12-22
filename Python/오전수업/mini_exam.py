# 미니 시험

# 딕셔널이ㅔ 저장하기 (키, value 알아서)
# 1. 이메일의 도메인 몇개이고 무엇무엇 있는지 출력하기(중복없이) 
# 2. naver 도메인의 이메일을 사용하는 사람들이 사는 도시 이름만 출력하기
# 3. 성별이 여자이;ㄴ 사람중에서 대전 중구에 사는 사람 출력


# 함수
# - 파일 읽기 함수
# - 파일 읽어서 딕셔너리에 저장하는 함수
# - 1. 함수 - 이메일엘서 도메인 분리하는 함수, 중복제거 하고 출력하는 함수
# - 2. naver.com인 사람 차즌 함수
# - 3. 성별로 찾는 함수 (꼭 여자만 찾을 수 있으면 안됨, 남자를 찾고 싶으면 찾기 되야한다. 코드수정x)

# 파일 키
info = ["번호", "이름", "연락처", "이메일", "성별", "주소"]
dic1 = dict()


# 파일 읽기 함수
def readFile():
  file=[]
  global dic1
  with open("c:/test/member.txt","r",encoding="utf-8") as f:
    file=f.readlines()

  for i in range(len(file)):
    file[i] = file[i][:len(file[i])-1]
    file[i] = file[i].split(" ")

  dic1 = fileSave(file)
  # for i in dic1:
  #   print("{0} : {1}".format(i, dic1[i]))
  
  return dic1

# 파일 읽어서 딕셔너리에 저장하는 함수
def fileSave(f):
  dic = dict()
  global info
  for i in range(len(f)):
      dic[i+1] = dict(zip(info,f[i]))
  return dic

# 이메일에서 도메인 분리하는 함수
def domain(d):  
  li = list()
  data = list()
  for i in d:
    data.append(d[i]['이메일'])

  for i in data:
    li.append(i.split("@")[1])

  return li
  
# 이메일 중복 제거하고 출력하는 함수
def duplicationRemove(li):
  cnt = dict()
  res = list(set(li))

  for i in range(len(res)):
    domain = 0
    for j in range(len(li)):
      domain += res[i].count(li[j])
    print("{0} : {1}".format(res[i],domain))

  
  

# 이메일이 네이버인 사람 찾는 함수
def findNaver(d):
  for i in d:
    if "naver.com" == d[i]['이메일'].split("@")[1]:
      print(d[i]['주소'].split("-")[0])

# 성별 찾기
def findGender(d):
  gender = input("찾고싶은 성별을 입력하세요 (남/여) : ")
  for i in d:
    if gender == d[i]['성별']:
      if '중구' == d[i]['주소'].split("-")[1] and '대전' == d[i]['주소'].split("-")[0]:
        print(d[i])

rf = readFile()
dm = domain(rf)
dr = duplicationRemove(dm)
print("======================")
findNaver(rf)
print("======================")
findGender(rf)
