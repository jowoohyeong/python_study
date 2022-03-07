# 모듈 형태로 되어있는 함수들의 집합
def say_name(name):
    print("안녕하세요, " + name)

def say_hello(name, msg):
    print("안녕하세요, " + name + msg)

def get_sum(start, end):
    sum = 0
    for i in range(start, end + 1):
        sum += i
    return sum
