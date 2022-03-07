item1 = int(input("첫번쩨 정수 입력: "))
item2 = int(input("두번째 정수 입력: "))

# 3의 배수이면서 4의 배수 제외 출력

for i in range(item1, item2+1):
    if i % 3 !=  0 or i % 4 != 0:
        print(i, end=" ")