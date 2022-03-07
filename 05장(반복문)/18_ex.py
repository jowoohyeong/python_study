
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print("")

# format() 함수 이용
# format 함수는 {} 이용하고 숫자도 같이 이용함.
# 인덱스를 활용하여 해당하는 값들을 출력할 수 있다.
print("정수값 : {}, string : {}, float : {}".format(10, "안녕하세요", 10.0))
print("정수값 : {0}, string : {1}, float : {2}".format(10, "안녕하세요", 10.0))
print("정수값 : {2}, string : {0}, float : {1}".format(10, "안녕하세요", 12.345))

# format 함수는 공간확보 및 0으로 채우는 기능도 지원함
# : 을 기준으로 우측에 > 혹은 < 부등호를 사용해서 방향을 지정해줄 수 있다.
print("숫자 '{:>5d}'".format(300))  # 오른쪽으로 밀어서 출력
print("숫자 '{:<5d}'".format(300))  # 왼쪽으로 밀어서 출력

for i in range(5):
    print("{:<}".format("*" * (i+1)))
print("------------------------")
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
print("-2번째 format")
for i in range(6, 0, -1):
    print("{:<5}".format("*" * (i-1)))