# 정수입력 2개
# max, min 함수 만들어보기

# 함수의 목록이 정의되어 있는 모듈을 import할 때는 항상 개바롴드 상위에 위치해야한다.
from calc import *

num1 = int(input("정수입력: "))
num2 = int(input("정수입력: "))

print("큰 값은: ", get_max(num1, num2))
print("작은 값은: ", get_min(num1, num2))

# 거듭제곱 값 power()
print("거듭제곱 값 : ", power(num1, num2))