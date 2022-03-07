def test(n1, n2): # 함수 매개변수도 지역변수의 일종
    global a
    a = 20
    n1 = n2
    n2 = n1
    b = 10
    print(a, b, n1, n2)

a, b, n1, n2 = 10, 20, 77, 88

test(n1, n2)
print(a,b,n1,n2)