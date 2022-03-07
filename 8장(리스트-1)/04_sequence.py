# 시퀀스 자료형 : 순서를 가지는 요소로 구성된 자료형
# 문자열, 바이트 시퀀스, 바이트배열, 리스트, 튜플, range() 객체

words = "Nice To Meet You!"
print(words[0], words[5], words[-1])
print(len(words))

li = ["바나나", "사과", "멜론", "토마토"]
print(li[0], li[-1])
print(len(li))

li1 = [1, 2]
li2 = [3, 4, 5]
li3 = li1 + li2
print("주소값 li1 : ", id(li1))
print("주소값 li2 : ", id(li2))
print("주소값 li3 : ", id(li3))

# 시퀀스 자료형에서 해당하는 값을 반복시키기
print(["안녕", "hi"] * 3)

# in 연산자와 not in 연산자
print(10 in [10, 23, 4])
print(10 not in [10, 23, 4])

# 최대값과 최소값  / 문자열 리스트에서는 의미없는 함수
print(max([1, 5, 6, -7, 3]))
print(min([1, 5, 6, -7, 3]))

# 반복문의 시퀀스 자료형이 올 수 잇다.
for i in "일이삼":
    print(i)
