# 튜플 실습
# 특징 : 리스트에 반하여 변경 불가, 리스트에 비해 속도가 빠름
# 튜플도 시퀀스의 일종
# *, +, min(), max(), len(), cmp(), tuple() 연산과 내장함수 사용가능
colors = ("red", "blue", "yellow")
print(colors)
print(type(colors))

numbers = (1,2,3,4,5)
print(numbers)

# 여러 자료형 가능
tuple1 = (1, 2.2, "하이")

# 공백 튜플 만들기
t1 = ()
t2 = (10,)
t3 = (10)
print(type(t1))
print(type(t2))
print(type(t3))

li = [1,2,3,4,5]
t4 = tuple(li)
print(li)
print(t4)

# 내장 튜플
print("-----------------------")
t1 = (1, 2.2, "hi")
t2 = (3.3, 4.4, 5.5)
t3 = t1, t2
print("t1의 주소: ", id(t1))
print("t2의 주소: ", id(t2))
print("t3의 주소: ", id(t3))
print("t3[0]의 주소: ", id(t3[0]))
print("t3[1]의 주소: ", id(t3[1]))

print("-----------------------")
print("t1의 길이: ", len(t1))

# 자료형이 다른 값이 포함되어 있으면 에러
print("max(t2): ", max(t2))
t4 = t1+t2
print("t1 + t2 = t4 ->", t4)
print("t1 * 2 = ", t1*2)

if 3.3 in t2:
    print("3.3가 t2에 존재한다")

for value in t2:
    print(value, end=" ")
print("")
print(t4[2])
print(t4[-1])

# 슬라이싱
print(t4[4:6])
print(t4[-3:-1])
print(t4[0:5])

# cmp() 함수는 미지원
c1 = (1, 2.2, 3)
c2 = (1, 2.2, 3)

# dir() 함수는 사용할 수 있는 함수를 출력해줌
print(dir(c1))
print(c1.__eq__(c2))