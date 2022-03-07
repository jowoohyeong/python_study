# 임의의 숫자게임

from random import *

cnt = 0
num = -1
ranNum = randint(1, 100);
print("1부터 100사이 숫자를 맞추기")
print("정답 : %d" %ranNum)
while num != ranNum:
    num = int(input("정수 입력: "))
    cnt += 1
    if num < ranNum:
        print("숫자가 작다")
    elif num > ranNum:
        print("숫자가 크다")
    else:
        print("%d 번만에 맞췄습니다." % cnt)
        code = input("게임 재시작 : y, 종료 : n 입력: ")
        if code == "n":
            break
        else:
            print("재시작합니다.")
            print("1부터 100사이 숫자를 맞추기")
            ranNum = randint(1, 100);
            print("정답 : %d" % ranNum)
            cnt = 0

print("종료합니다.")
