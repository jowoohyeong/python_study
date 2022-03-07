# 리스트 함축 / 수학에서의 집합과 유사

# 일반 코드
squares= []
for x in range(1, 11):
    squares.append((x **2 ))

# 리스트 함축 코드
print(squares)
s = [x**2 for x in range(1, 11)]
print(s)

# 조건 리스트 함축 / 홀수 출력
s1 = [x for x in range(21) if x % 2 == 1]
print(s1)

s2 = [x for x in range(21) if x % 2 == 0]
print(s2)

gugudan = [i*j for i in range(1, 10)
               for j in range(1, 10)]
print(gugudan)