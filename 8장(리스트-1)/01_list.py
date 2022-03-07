# 리스트 실습
# 대량의 데이터를 저장할 수 있는 공간

scores = []
print("리스트 초기화 값 : ", scores)

scores.append(30)
print("리스트 값 : ", scores)

scores.append("안녕")
print("리스트 값 : ", scores)

scores.append(10.123)
print("리스트 값 : ", scores)
print("리스트 크기 : ", len(scores))

scores[0] = 15
print("리스트 값 : ", scores)

# 리스트 값 순회 출력
for i in range(len(scores)):
    print(i, scores[i])

# 속성값 출력
for element in scores:
    print(element, end=" ")
print()

# 입력받기
# nums = []
# for i in range(5):
#     nums.append(int(input("정수 입력: ")))
# print(nums)

# list 클래스(속성(멤버변수), 기능(멤버메서드), 생성자) 생성자를 이용한 리스트 만들기
li1 = list()
print(li1)

li2 = list("안녕")
print(li2)

li3 = list(range(0,5))
print(li3)

print("내장 리스트 실습")
li1 = [12, 12.7566, "안녕"]
print(li1)

li2 = [["서울", 1], ["뉴욕", 2], ["파리", 3]]

for i in range(len(li2)):
    for j in range(len(li2[i])):
        print(li2[i][j], end=" ")   # 2중 내장리스트 li2[i][j]는 변수와 동일하다
    print()
