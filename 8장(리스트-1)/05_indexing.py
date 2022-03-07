# 인덱싱 : 리스트에서 하나의 요소를 인덱스를 통해 참조하는 것
li = ["안녕", "조우형", 10, 100, -1]
print(li[2])
print(li[-2])       #아래와 같음
print(li[-2 + len(li)])

# 슬라이싱(slicing) : 리스트 범위 안에서 범위를 지정하여 원하는 요소들을 선택
temp = ["안녕", "조우형", 10, 100, -1, False, True]
print("temp 주소값 : ", id(temp))

t = temp[2:5]
print("t 주소값 : ", id(t))
print("슬라이싱 : ", t)

t = temp[:5]
print("t 주소값 : ", id(t))
print("슬라이싱 : ", t)

t = temp[2:]
print("t 주소값 : ", id(t))
print("슬라이싱 : ", t)

words = list("abcdefg")
print("words 변경 전 주소값 : ", id(words))
words[1:3] = list("BCD")
print("words 변경 후 주소값 : ", id(words))
print(words)

words[:] = []
print("범위 선택 시 주소 값: ", id(words))
words = []
print("범위 미선택 시 주소 값: ", id(words))
