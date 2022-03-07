# 키워드 인수 keyword argument
# 통상 프로그래밍 언어라면 함수의 매개변수의 위치를 기준으로 ㅐ서
# 해당 인수를 매칭해줌으로써 함수에 값이 전달(복사)된다.
# 위치 인수 방식 positional argument 이라고 한다.

def calc(x,y,z):
    return x-y+z

print(calc(10, 100, 1000))

# 장점 : 매개변수의 위치에 얽매이지 않고 직접 키워드값에 값을 할당하므로써 함수 호출이 이러우진다.
print(calc(x=10, z=100, y=1000))