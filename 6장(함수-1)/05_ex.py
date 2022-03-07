# 정수 입력:
# 소수를 판별하는 함수 is_prime() 작성
# 소수면 True, 아니면 False

num = int(input("정수 입력: "))

def is_prime(x):
    if x < 3:
        return True
    for i in range(2, x):
        if x % i == 0:
            return False

    return True

print("소수 판별: ", is_prime(num))