# 리스트 일치 검사
# 리스트 길이 다르면 무조건 False

# 같은 자료형만 가능
item1 = [10, 20, 30]
item2 = [10, 20, 30]
print(item1 == item2)

item1 = [10, 20, 30]
item2 = [10, 20, 29]
print(item1 > item2)

# 아스키 코드를 기준으로 비교
w1 = list("abc")
w2 = list("abd")
print(w1 > w2)
print(ord("c"))
print(ord("d"))

print(chr(99))
print(chr(100))

# 리스트 정렬
# sort() 원본 리스트의 값이 변경됨, 반환 값 X
a = [80, 90, 100, -70, -50]
a2 = [80, 90, 100, -70, -50]

sa = a.sort()
print("오름차순 sort() : ", a)
a2.sort(reverse=True)
print("내림차순 sort() : ", a2)
print("sort() 반환 값: ", sa)

# sorted() : 내장함수, 원본 리스트는 유지하고 반환 값 O
a = [80, 70, 140, 43, -70, -50]
a2 = [80, 70, 100, 43, -70, -50]
b = sorted(a)
b2 = sorted(a, reverse=True)
print(a)
print("오름차순 sorted() : ", b)
print("내림차순 sorted() : ", b2)

# 리스트 객체의 reverse() 리스트 요소 뒤집기
arr = [1, 2, 3, 5, 8, 9]
print("arr: ", arr)
arr.reverse()
print("arr.resever(): ", arr)

# 문자열 정렬 / 유니코드 기준
li = "하와이 폭포 가나 한국".split()
li2 = sorted(li, key=str.lower)
print(li2)