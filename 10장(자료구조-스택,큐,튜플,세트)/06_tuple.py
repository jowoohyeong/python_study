# 튜플 대입 연산 실습
# 튜플 패킹 : 튜플에 값을 저장하는 과정
# 튜플 언패킹 : 튜플에서 값을 추출해서 변수에 대입하는 과정

# 튜플을 이용한 값 교환 / 인자값이 서로 맞게끔 해야한다. (x, y ,z) = (10, 20) 은 error
a, b = 100, 200
print(a, b)
a, b = b, a
print(a, b)
person = ("woo", 23, "대학생")
name, age, grade = person
print(name, age, grade)