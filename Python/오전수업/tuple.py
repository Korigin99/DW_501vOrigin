
# f = open("c:/test/qeustion.txt", "r", encoding="utf-8") # 쓰기 - w , 읽기 - r , 추가 - a

#line = f.readlines() # 파일 전체 읽어오기, 한 줄씩 가져와서 리스트에 저장
#line = f.readline() # 파일 한줗  읽어오기
# line = f.readlines()
# print(line)

# f.close() # 파일을 열어서 다 읽었다면 닫아야한다.
""" 
file=[]
with open("c:/test/question.txt","r",encoding="utf-8") as f:
  file=f.readlines()

for i in range(len(file)):
  file[i] = file[i][:len(file[i])-1] # 문자열 슬라이싱 "banana"[2:] -> "nana" , "banana"[2:4] -> "na"
                                      # "banana"[:4] -> "bana"
  file[i] = file[i].split(" ")

 """
# print(file)

# 작성자 또는 제품명으로 검색하여 해당 문의글을 전체 출력하기
""" 
search = input("작성자 또는 제품명을 검색해 주세요 : ")
res = ""
tmp = ""

for i in range(len(file)):
  for j in range(len(file[i])):
    if(search in file[i][j] ):
      res = "작성자 : " + file[i][1] + "\n제목 : " + file[i][0] + "\n작성일 : " + file[i][3] + "\n문의글 : " + file[i][2] + "\n=====================\n답변 : " + file[i][4] + "\n답변일 : " + file[i][5]
      if(res != tmp):
        tmp = res
        print(tmp)
 """

# 다른 답안
""" 
search = input("작성자 또는 제품명 : ")

for qus in file:
   for i in range(len(qus)):
    if search in qus[i]:
      print("작성자 : {0}\n제목 : {1}\n 작성일 : {2}\n문의글 : {3}\n===================\n답변 : {4}\n답변일 : {5}".format(qus[0],qus[1],qus[3],qus[2],qus[4],qus[5]))
      break

"""


"""

  튜플 - 리스트처럼 데이터를 저장해두는 구조이다.
  리스트처럼 여러데이터를 복합적으로 저장 가능하다.
  하지만 튜플은 리스트와 다르게 변경이 안된다.
  데이터 변경이 안될 뿐 나머지는 리스트와 동일하다.
  리스트의 표현태그는 [] 이고, 튜플은 () 이다.

  튜플 생성

"""

# 튜플 생성
tu = "새신발", "밟혔다."
print(tu)

tu2 = ("그래서", "주먹으로쳤다.")
print(tu2)
tu3 = ("아프다")
print(type(tu3))
tu4=("하녀복장",)
print(type(tu4))

tu5 = ("그리고", "난", "발목을 차였다","혼신의주먹을날릴뻔")
a,b,c,d = tu5
print(a,b,c,d)
print(tu5[2])
print(tu5[1:])
# 변경 추가 불가능
print(tu5.count("난"))
print(tu5.index("발목을 차였다"))