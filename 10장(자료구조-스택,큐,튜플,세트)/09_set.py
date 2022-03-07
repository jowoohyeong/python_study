# set 은 개념은 수학의 집합과 같은 개념
# 특징: 중복 허용 x, 순서유지 x

# 세트는 입력순서와 동일하게 출력하지 않음
s1 = {2,1,34,5,3}
print(s1, len(s1))
s2 = {"안녕", "하이","사람", "자동차"}
print(s2, len(s2))

# 중복 불가
s3 = {1,2,1,21,3,1,2,31,"안녕", "안녕", "자동차", "자동차","나이"}
print(s3)

if "안녕" in s3:
    print("s3에는 '안녕'이 존재한다")

# set 요소 for문 출력
for value in s3:
    print(value, end=" ")

print()
print("--------------------------")

# set는 순서를 유지하지 않기 때문에 인덱싱과 슬라이싱 불가 ////// s3[1] error
# 비어있는 세트 만들기
s4 = set()
# set는 add()를 통해 요소 추가
# 모든 요소를 해싱기법을 이용하여 저장하고 관리한다. 그래서 요소는 해싱가능(hashable) 해야한다.
# 해싱이란 각각의 객체에 식별할 수 있는 해쉬코드를 부여하여 객체를 테이블에 저장하는 것이다.
s4.add("봄")
s4.add("여름")
s4.add("가을")
s4.add("겨울")
print(s4)

# 세트는 요소 해싱가능하려면 해쉬코드를 가져야 한다.
# 그 값이 변경되면 안되기 때문에 변경가능한 항목을 가지면 안된다.
# 리스트를 요소로 가지지 못함   // s5 = {1.2, 2, "자동차", [10, 20]}  error
s5 = {1.2, 2, "자동차", (10, 20)}      # 튜플은 가능
print(s5)

# 여러 요소를 추가하려면 update() 사용가능
# 문자열 []에 "인간" 포함하면 한 단어로 세트에 저장된다.
# 문자열 []에 "인간"을 포함하지 않으면 한 단어로 저장되지 않는다.
s6 = set()
s6.update(["인간", 1, 34, 5, 6])
s6.update("인간",[1, 34, 5, 6])
print("s6: ", s6)

# 세트 요소 삭제 discord(), remove() -- 둘다 반환값 X
s6.discard("인간")
print("discard: ", s6)

# 없는 요소를 삭제시도시 remove()는 KeyError를 발생시킨다.
s6.remove(34)
print("34 remove: ", s6)

# 세트 초기화
s6.clear()
print(len(s6))