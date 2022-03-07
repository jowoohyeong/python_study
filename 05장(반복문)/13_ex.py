# 임의의 개수의 성적 입력 -> 합계와 평균 계산

print("종료시 음수")
num = 1
sum = 0
cnt = 0
while num > 0:
    num = int(input(str(cnt+1)+"번째 성적 입력: "))
    if num < 0:
        break
    sum += num
    cnt += 1

print("%d명의 성적의 합계는 %d, 평균은 %.2f점" %(cnt, sum, sum/cnt))