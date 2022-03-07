# Counter 모듈은 시퀀스 자료형의 데이터의 값의 개수를 딕셔너리 형태로 반환해는 자료구조이다.
# 같은 값이 몇 개가 존재하는지 쉽게 알아보고자 할 때 사용하면 좋다.

from collections import Counter
from itertools import repeat, chain
text = list("high school")
c = Counter(text)
print(c)
print(type(c))

# 시퀀스 자료형에서 다른 특수문자의 개수를 알고 싶을때도 사용하면 된다.
print("h의 개수: ", c["h"])

print("-----------------")
# Counter() 객체를 만들 때, 값 개수와 같은 형태로 입력도 가능
c = Counter(b=2, c=5, d=3)
print(c)
print(list(c.elements()))

print(list(repeat([1,2,3], 3)))
print(list(chain.from_iterable(repeat(number, 3) for number in [1,2,3])))

# elements() 는 Counter() 객체로 주어진 값의 요소에 해당하는 값을 풀어서 반환을 한다.
# 요소는 무작위적으로 반환하며 요소의 수가 1보다 작을 경우에는 elements()는 이를 출력하지 않는다.
# 대소문자 구별, sorted() 정렬이 되어진다.
print(sorted(c.elements()))


text = "abcdd repeat count you can do it nice to meet you. A count " \
    "telep call do you me me like you".lower().split()

print(text)
print(Counter(text))

print("----------------------")
# 값=개수 형태로 Counter()객체를 만들 때는 문자열은 매개변수로 쓸 수가 없다.
# //a ="가" Counter(a=2) error
# 문자열 자체를 매개변수로 넣어주는 것은 가능하다.
count = Counter("가나다라마바가나")
print(count)
# 딕셔너리 형태로 Counter 형태로 객체를 생성하는 방법
count = Counter({"가":2, "나":3})
print(count)
print(list(count.elements()))
