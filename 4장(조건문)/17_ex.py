# 사용자로부터 정수 입력받고 음수, 0, 양수 중에 어떤 값인지 출력

number = int(input("정수 입력: "))

if number < 0:
    print("음수")
elif number == 0:
    print("0")
else:
    print("양수")