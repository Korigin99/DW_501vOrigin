""" print("aa")
x = 9
print("output : " + str(x))


a = 3.14
print("float : {0}".format(a))
print("float : {0:.1f}".format(a))

print(type(a))

name = "김기원"
print("이름 : {0:s}".format(name))
print("이름 : " + name)

memo="이 이정수를 때렸다"

result = name + memo
print(result)

res_len = len(result)
print(res_len)

temp1 = result.split()
# split의 기본 값은 띄어쓰기다.
print(temp1)

temp2 = result.split(" ",1)
# 띄어쓰기로 분리하되 한번만 분할
print(temp2)

print(" {0}".format(",".join(temp1)))

num = int(input("숫자를 입력하세요")) # input은 입력함수이다. 결과는 문자열로 반환한다.
print(type(num)) """

""" 문제1 . 국어, 수학, 영어 세 과목 점수 입력 받아서 평균을 구하여 출력 """

kor = int(input("국어 점수를 입력하세요 : "))
math = int(input("수학 점수를 입력하세요 : "))
eng = int(input("영어 점수를 입력하세요 : "))

total = kor + math + eng
avg = total/3
print("평균 : {0} {0}".format(total,avg))
print("평균 : " + str((kor+math+eng)/3))

