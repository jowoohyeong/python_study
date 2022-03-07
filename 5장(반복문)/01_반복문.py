# 반복문 (iteration)에 대한 실습
# in 다음에 오는 것을 시퀀스라고 한다.
# 시쿼스에 올 수 있는 것은 리스트, 문자열이 존재한다.

for i in range(5):
    print("안녕하세요")

# range() 함수의 타입은 range 객체타입이다.
print(type(range(5)))

# 문자열 리스트를 시퀀스로 가질 때의 for문
s = ["서울", "부산", "대구"]
for area in s:
    print(area)
# 줄바꿈 제거
for area in s:
    print(area, end=" ")
