# 소수 2부터 2000까지의 더하기
# 마지막 소수와 최대합 출력
# 마지막으로 더해지는 소수는 얼마
# 더블루프, 조건식
start_num = 0
hap = 0
lastData = 0
for num in range(2, 2001):
    for start_num in range(2, num+1):
        # 배수나 소수인지를 걸러내는 조건식
        if num % start_num == 0:
            break
    # 아래 조건이 참이라는 것을 자기자신으로 나눠서 나머지가 0이 나왔다는 것은
    # 바로 소수를 의미하므로 아래 코드가 실행됨
    if num == start_num:
        hap += start_num
        lastData = start_num
        print("소수 : ", start_num, ", 합 : ", hap, ", 마지막 합 : ", lastData)

