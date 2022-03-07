# 문자열 전달 실습
# 문자열도 숫자형 객체와 동일한 immutable object 형태이다.
# 파이썬은 모든 것을 객체로 판단하기 떄문에 타 언어의 call by value 개념과 다르다.
# 파이썬의 이런 특성은 call by objective 라고 칭한다.
def change(string):
    print("함수 내부 연산 전 : ", string, id(string))
    string += ", to you"
    print("함수 내부 연산 후: ", string, id(string))

msg = "hi hello"
print("함수 호출 전: ", msg, id(msg))
change(msg)
print("함수 호출 후: ", msg, id(msg))
