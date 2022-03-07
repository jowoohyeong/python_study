# 메서드 실습
from collections import Counter

# update() : Counter 객체의 값을 갱신
count = Counter()
count.update("안녕하세요")
print(count)

count.update({"안":3, "요": 5, "우":3})
print(count)
print("--------------------------")

# most_common(n) : 입력된 값의 요소 중에서 빈도수가 높은 순으로 상위 n개를 리스트안에 튜플 형태로 반환하는 메서드
count = Counter("apple, orange, grape") 
# 매개변수를 주지 않았을 때 전체 문자열을 대상으로 값과 빈도수를 출력
print(count.most_common())
print(count.most_common(3))

print("--------------------------")
# subtract() : 단어 그대로 요소 값을 빼는 것
# 요소가 없을 경우 음수 출력
c1 = Counter("반갑습니다. 안녕하세요")
c2 = Counter("반갑다. 친구야")
c1.subtract(c2)
print(type(c1))
print(c1)

print("--------------------------")
# Counter() 객체는 산술/집합 연산 가능
# 덧셈
c1 = Counter("a b c d e a".split())
c2 = Counter("apple")
print(c1)
print(c2)
print(c1+c2)

print("--------------------------")
# 뺄셈        //연산자로 뺄셈시 음수의 값은 출력안함. subtract 와 다른 점
c1 = Counter("a b c d e a".split())
c2 = Counter("apple")
print(c1)
print(c2)
print(c1-c2)

print("--------------------------")
# 교집합과 합집합
c1 = Counter("abcdefg")
c2 = Counter("abcd가나다라")
print(c1 & c2)
print(c1 | c2)
print("--------------------------")
# 곱하기와 나누기, %는 지원하지 않는다.

