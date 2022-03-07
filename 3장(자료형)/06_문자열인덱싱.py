# 문자열의 인덱싱
# 인덱싱이란 문자열에서 문자를 추출하는데 문자열에는 가각에 해당하는 문자에 번호(인덱스)가 존재
# [index] 하면 문자열에서 문자를 추출할 수 있다.

word = "pythonstudy"
print(len(word))
print(word[5])
print(word[-1])

# 문자열의 인덱스 범위 밖에 값을 주면 index out of range 오류발생
# 파이썬은 한 번 작성된 문자열 변경 불가

a = input("문자열입력 : ")
b = input("문자열입력 : ")
c = input("문자열입력 : ")
temp = a[0] + b[0] + c[0]
print(temp)