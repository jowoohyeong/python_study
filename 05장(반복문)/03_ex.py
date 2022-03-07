# 1부터 사용자 입력한 수까지 합

num = int(input("정수 입력: "))
sum = 0
for i in range(num+1):
    sum += i

print("합은 : ", sum)
