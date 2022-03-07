# 매개변수는 지역변수의 일종이다!

def list_test(li):
    print("함수 내부 1: ", li, id(li))
    li = [1,2,3,4]
    print("함수 내부 2: ", li, id(li))

li =[10,20,30,40]
list_test(li)
print("함수 외부: ", li, id(li))