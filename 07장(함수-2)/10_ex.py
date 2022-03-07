# 원의 면적, 원의 둘레 구하는 프로그램
# PI = 3.141592 전역변수 선언

PI = 3.141592
# 프로그램 시작 함수
def main():
    print("원의 면적: ", circleArea(5))
    print("원의 둘레: ", circleCircumference(5))
# 원의 면적
def circleArea(r):
    return PI * (r **2)
# 원의 둘레
def circleCircumference(r):
    return 2 * PI * r

#
main()