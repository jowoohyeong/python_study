# 무명함수(익명함수, anonymous) 실습
# 함수명이 없고, 구현부만 존재
# lambda 실습
# 무명함수는 print()함수같은 일반함수 호출 불가, 연산만 가능
# 전역변수 참조 불가

get_sum = lambda x, y: x+y
# 람다식 리스트 데이터
li = [ lambda x: x**2, lambda x: x**3, lambda x: x**4 ]
def main():
    # 람다함수는 디폴트인자 불가
    x, y = 10, 50
    print("정수의 합: ", get_sum(x, y))
    print("정수의 합: ", get_sum(100, 500))
    # 실질적인 람다식 이용사례
    print("정수의 합: ", (lambda x, y: x+y)(1000,5000))

    for f in li:
        print(f(10))


main()

