# 섭씨온도 -> 화시온도 함수

num = int(input("정수입력: "))

def FtoC(a):
    return (5.0 * (a - 32.0)) / 9.0

print("화씨온도 %d 를 섭씨온도로 변환한 값 : %.2f" % (num, FtoC(num)) )