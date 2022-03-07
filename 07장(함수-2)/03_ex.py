# call by reference 실습
# 함수 호출시, 실질적인 주소값이 넘어가서 호출한 곳에 영향을 끼치는 형태
# 파이썬에서는 함수의 매개변수값이 전부 객체인데 list, dictionary와 같은 mutable object
# 즉 변경가능한 객체 call by objective-reference 라고 함

def change(li):
    print("함수 내부 연산 전 : ", li, id(li))
    li += [100, 200]
    print("함수 내부 연산 후 : ", li, id(li))

list = [2, 5, "hello"]
print("함수 호출 전: ", list, id(list))
change(list)
print("함수 호출 후: ", list, id(list))

