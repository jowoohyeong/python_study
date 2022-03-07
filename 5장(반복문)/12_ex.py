# while 문 실습

i = 0
while i < 5:
    print("반갑습니다.")
    i += 1
print("반복 종료")

i = 0
while i < 10:
    print(i, end=" ")
    i += 1
print()

i = 0
sum = 0
while i < 10:
    sum += i
    i += 1

print(sum)
# while 팩토리얼
fact = 1
i = 1
while i < 10:
    fact *= i
    i += 1
print("10! = %d" % fact)

# 구구단
print("구구단 3단")
i = 3
while i < 10:
    print("3 * %d = %2d" % (i, 3*i))
    i += 1

# while 피보나치
i = 0
n1 = 1
n2 = 1
n3 = 1
while i < 5:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    i += 1

print("5 까지 피보나치 수열 : %d" % n3)

i = 1
sum = 0
while i < 101:
    i += 1
    if i % 3 == 0:
        sum += i

print("3의 배수의 합: %d" % sum)

# 1234 - > (1+2+3+4)
num = 1234
sum = 0
while num > 0:
    sum += num % 10
    num = num // 10
print("1234 -> %d" % sum)