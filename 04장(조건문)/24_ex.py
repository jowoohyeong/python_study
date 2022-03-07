# 숫자 추측 게임

from random import *

randNum = randint(1, 100)

print("숫자를 맞춰보세요(1~100)")
print(randNum)
cnt = 0
while True:
    num = int(input("입력: "))
    cnt += 1
    if randNum == num:
        print("정답.\n게임을 종료합니다.(시도횟수 : ", cnt,")")
        break
    elif randNum > num:
        print("입력한 숫자가 작습니다.")
    else:
        print("입력한 숫자가 큽니다..")
