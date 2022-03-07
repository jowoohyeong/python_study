# 1. 상품 금액 입력
# 2. 상품 총가격 계산
# 3. while
# 4. "끝" 입력시 종료
from operator import eq
# from operator

total = 0
price = 1
while True:
    price = input("상품금액 입력: ")
    if eq(price, "끝"):      # price=="끝" 과 동일한 코드  operator.eq(a, b)
        print("총 상품가격은 %d원입니다." % total)
        break
    total += int(price)
