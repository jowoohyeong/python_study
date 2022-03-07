# 구의 부피 계산

import math
n = int(input("정수 입력: "))
def sphereVolume(r):
    return 4/3 * math.pi * (r**3)

print("구의 부피: ", round(sphereVolume(n), 2))