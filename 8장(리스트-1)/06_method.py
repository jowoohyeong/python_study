# 리스트의 기초 연산들

li = ["TV", "오디오", "PC", "키보드"]
print("li의 주소 : ", id(li))
print(li)

# append() 리스트의 마지막에 삽입
li.append("마우스")
print("li의 주소 : ", id(li))
print(li)

# insert() 원하는 인덱스 위치에 요소 추가
li.insert(1, "휴대폰")
print("li의 주소 : ", id(li))
print(li)

print("----------")
item1 = ["안녕", "사람", "인형", "나무", "가죽", "하늘", "공백", "안녕", "안녕"]
if "나무" in item1:
    print("나무가 존재한다")
else:
    print("나무가 없다")

# index() 리스트에서 요소를 찾을 때
print(item1)
if "하늘" in item1:
    index = item1.index("하늘")
    print(index, "번째 위치에 하늘 존재")
print("----------")

# 요소 삭제 pop() 인덱스 해당 요소 삭제 반환O
element = item1.pop(0)
print("pop element: ", element)
print(item1)

# 요소 삭제 remove(element) element 일치 요소 삭제, 반환X
element = item1.remove("인형")
print("remove element: ", element)
print(item1)
while "안녕" in item1:
    item1.remove("안녕")
print(item1)

# 요소 삭제 del listNam[idx] 인덱스 해당 요소 삭제, 반환X
del item1[0:3]
print("del element: ", element)
print(item1)

# clear() 모든 요소 삭제, 반환요소 x
item1.clear()
print(item1)

# count() 리스트에 포함된 특정 요소 개수
item2 = ["안녕", "사람", "인형", "나무", "가죽", "하늘", "공백", "안녕", "안녕"]
cnt = item2.count("안녕")
print("'안녕'의 개수: ",cnt)

# extend(args) 리스트를 더하는 함수( +=)
item1 = [1, 3, 54, 23, 123]
print(id(item1))
item1.extend(item2)
print(id(item1))
print(item1)