# 구구단

num = int(input("정수 입력: "))

for i in range(1, 10):
    if 2 > num or num > 9:
        print("2~9단 가능합니다.")
        break
    print(num, " * ", i, " = ", num*i)
