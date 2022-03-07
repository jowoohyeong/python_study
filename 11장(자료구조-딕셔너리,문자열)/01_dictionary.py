# dictionary : 사전과 유사
# key : value 의 쌍을 저장할 수 있는 객체

# 생성 방법 // 리스트로 키 값을 사용할 수 없다. 키 값은 변경 불가능한 객체이어야 한다.
d1 = {1:"사과", 2:"토마토", 3:"오렌지"}
print(d1)

# 키 값을 문자열, 튜플로 사용가능하지만 권장하지 않음
d2 = {1:"사과", "2" : "토마토", (3, ):"오렌지"}
print(d2)

# 공백 dictionary
d3 = {}

# 항목 추출     // 없는 키 값으로 호출시 get은 None, 인덱스로 호출시 KeyError
d4 = {1:"사과", 2:"토마토", 3:"오렌지"}
print("d4[1]: ", d4[1])
print("d4.get(2): ", d4.get(2))

# 존재하지 않은 키 값을 디폴트 값으로 사용하는 방법
a = d4.get(5, "파인애플")
print(a)

# 존재 유무 확인
print(1 in d4)
print(4 not in d4)

# 항목 추가, 변경 가능 객체
d5 = d4.copy()
print("요소 추가 전: ", d5, id(d5))
d5[3] = "배"
print("요소 추가 후: ", d5, id(d5))

print("---------------")
# 요소를 삭제해도 주소는 그대로
d6 = d1.copy()
print(d6.pop(2))
print("---------------")
d7 = d1.copy()
del d7[1]
print(d7)
print("---------------")
print("요소 초기화 전 주소: ", d7, id(d7))
print(d7.clear())
print("요소 초기화 후 주소: ", d7, id(d7))
