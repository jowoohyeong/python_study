from fibo import *


# __name__은 내장 전역변수로 인터프리터가 만들어 놓은 것
# import fibo
def main():
    fib(1000)
    print(sum(10))
    print(fib.__name__)


# 실행파일에서는 __name__ 이라는 내장 전역변수가 __main__ 값을 지니게 된다!!!!!!!!!!!!!
print(__name__)

if __name__ == "__main__":  # 프로그램의 시작점이 되는 형태
    main()