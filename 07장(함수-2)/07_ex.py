# 지역변수와 전역변수 실습
def testGlobal():
    global text
    print("testglobal(): ", text)
    text = "global 공부"
    print("testglobal(): ", text)

text = "파이썬 공부"

testGlobal()
print("global 호출 후:", text)
