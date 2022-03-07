# 1~100까지 누적값 구하기
# 값이 2000이상이 되면 break
sum = 0
# breakpoint(중단점)는 디버깅(에러를 잡는 과정)에 아주 효율적으로 사용할 수 있다.
# Run -> Debug -> F7을 눌러가면서 한 단계씩 확인 가능
for i in range(1, 101):
    sum += i
    if sum > 2000:
        print("마지막으로 더해지는 i 값 = ", i)
        break

print(sum)