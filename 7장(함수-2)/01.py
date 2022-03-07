# 값에 의한 호출 call by value
# 값에 의한 전달 pass by value
# 동일한 개념 함수를 호출할 때, 값이 복사됨
# 호출한 곳에 영향을 끼치지 않음

def change(num):
    num += 10
    print("함수 내부: ", num, id(num))
    return num

# id()함수는 매개변수 값으로 객체를 받아서 그 객체의 고유한 주소값을 반환
n = 10
print("함수 호출 전: ", n, id(n))
x  = change(n)
print("함수 호출 후: ", n, id(n))
print("함수 return 후: ", x, id(x))
