# 간단한 사칙연산
def add(x, y):
    return x+y
def sub(x, y):
    return x-y
def div(x, y):
    return round(x/y, 2)
def mul(x, y):
    return x*y

n1 = float(input("첫 번째 수 입력: "))
n2 = float(input("두 번째 수 입력: "))

while True:
    op = input("원하는 연산 입력: ")
    if op == "+":
        print(n1, op, n2, "=", add(n1, n2))
    elif op == "-":
        print(n1, op, n2, "=", sub(n1, n2))
    elif op == "*":
        print(n1, op, n2, "=", mul(n1, n2))
    elif op == "/":
        print(n1, op, n2, "=", div(n1, n2))
    else:
        print("잘못된 연산자")

    q = input("y or n: ")
    if q == "n":
        break