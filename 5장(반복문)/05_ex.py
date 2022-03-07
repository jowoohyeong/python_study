# for 문 factorial 팩토리얼

fact = 1.0
n = int(input("정수 입력: "))

for i in range(1, n + 1):
    fact *= i

print(fact)