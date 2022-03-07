from math import *
print(type(10))
print(type(10.123214))
print(type("string"))

# 반지름이 r인 구의 부피는 4/3 * pi * r의세제곱 공식
r = 5.0
volume = 4.0 / 3.0 * pi * r**3  # pow(r, 3)
print("구의부피: ", volume)

# 구의 겉넓의 공식 : 4 * pi * r의 제곱
outer_area = 4 * pi * pow(r, 2)
print("구의 겉넓이: " + str(outer_area))