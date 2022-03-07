# 원의 넓이와 둘레를 동시에 반환하는 함수
import math
def calcCircle(r):
    # 둘레
    circumstance = 2 * math.pi * r
    # 넓이
    area = math.pi * (r**2)
    return (circumstance, area)

if __name__ == "__main__":
    r = 10
    circumstance, area = calcCircle(r)
    print("반지름 %d의 넓이: %f,둘레: %f" % (r, area, circumstance))