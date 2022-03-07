# 지구랑 가장 가까운 별 = 프록시마 켄타우리와의 빛의 속도로 걸리는 시간
from math import *

# 빛의 속도 값 저장
light_speed = 300000
distance = 40 * 10**12
print(distance)
seconds = distance / light_speed
print("걸리는 시간(초): ", seconds)
light_year = seconds / (60 * 60 * 24 * 365)
print("걸리는 년도: ", light_year)