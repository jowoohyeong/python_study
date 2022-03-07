# 여러 개의 값을 반환하는 함수

# 함수는 한 가지의 값을 리턴한다.
# 아래의 함수는 리턴 값이 튜플 1개이다.
def tuple_return():
    return 1, "안녕", 5
    # == return (1,"안녕", 5)
a, b, c = tuple_return()
abc = tuple_return()
print(a, b, c)
print(abc)
print(type(abc))

li = list(abc)
li += "안녕"          # 리스트에 문자 하나씩 추가
li.append("안녕")     # 문자열 추가
print(li)