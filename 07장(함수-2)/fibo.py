# 피보나치 수열의 함수 선언 및 구현 - 모듈
# 모듈 : 함수나 변수를 모아둔 파일

def fib(n):
    a= 0
    b= 1
    while b < n:
        print(b, end=" ")
        a, b = b, a+b
    print()
def sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum