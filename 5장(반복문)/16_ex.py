# 플래그 변수를 사용한 무한 루프
# 1. 증속, 2.감속, 3. 중지---사용자의 입력
# 10씩 증속 및 감속

speed = 0
run = True
while run:
    num = int(input("1:증속\t|\t2:감속\t|\t3:중지: "))
    if num == 1:
        speed += 10
    elif num == 2:
        speed -= 10
        if speed < 0:
            print("속도가 음수일 수 없습니다.")
            speed = 0
    elif num == 3:
        run = False
    else:
        print("보기에 없는 입력!!")
    print("현재 상황 : %d" % speed)
print("최종 : %d" % speed)