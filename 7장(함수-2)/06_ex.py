# 전역변수 global variable

#
def testLocal():
    text = "local 공부"
    print("testlocal(): ", text)


text = "파이썬 공부"
testLocal()
print("local 호출 후:", text)
