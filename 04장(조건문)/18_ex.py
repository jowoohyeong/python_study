# 주사위 눈을 랜덤으로 발생, 해당 숫자를 출력
# randint() 함수 검색하여 사용법을 익힌 후 작성
from random import *
x = randint(1, 6)
print(x)

# random() 함수는 0.0~ 1 임의의 값을 float 형태로 반환해주는 함수
print(random())

# randrange(start, end, step) 함수는 start에서  end미만까지 step의 값에 따라 임의의 수를 반환
print(randrange(0, 101, 2))

# randerange(a) 함수는 0 ~ a미만까지 반환
print(randrange(10))