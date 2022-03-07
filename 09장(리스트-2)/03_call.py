# 값 호출, 참조 호출

def func(x):
    print("x=  ", x, ", address= ", id(x))
    x += 15
    print("x=  ", x, ", address= ", id(x))

y = 10
print("y=  ", y, ", address= ", id(y))
func(y)
print("y=  ", y, ", address= ", id(y))

def func2(x):
    print("x=  ", x, ", address= ", id(x))
    x.append(50)
    print("x=  ", x, ", address= ", id(x))

y = [10, 20, 30]
print("y=  ", y, ", address= ", id(y))
func2(y)
print("y=  ", y, ", address= ", id(y))