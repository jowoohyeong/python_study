# namedtuple 모듈은 튜플의 형태로 데이터를 구조화에 맞게끔 저장하는 자료구조

# 일반적인 튜플
person1 = ("조우형", 24, "남")
person2 = ("김영희", 22, "여")
for n in [person1, person2]:
    print("%s - %d - %s" % n)
print("--------------------")
from collections import namedtuple
# typename, field_names 생략가능
Person = namedtuple(typename="Person", field_names='name age gender')

# _make() : 기존에 생성된 namedtuple에 새로운 인스턴스를 생성해주는 메소드
P1 = Person._make(['Tom', 24, '남'])
P2 = Person._make(['Sally', 28, '여'])
P3 = Person._make(['Tom', 28, '남'])

# 인덱스를 통한 값변경은 불가하지만 _replace() 메소드로 값 변경 가능!
print("replace result before: ", P1)
P1 = P1._replace(name="Neo", age=23)
print("replace result after : ", P1)

# 생성된 Person namedtuple의 _fields 로써 Person에 있는 필드명 tuple() 형식으로 리턴
print(P1._fields)

# getattr()는 필드명으로 그 값을 출력 시 사용
print("P123.name: ", getattr(P1, 'name'), getattr(P2, 'name'), getattr(P3, 'name'))

# **(doulbe-star-operator)은 namedtuple() 딕셔너리 자료구조를 namedtuple() 변환하여 반환
dic = {'name':'Tony', 'age': 26, 'gender': "남"}
P4 = Person(**dic)
print(type(P4))
print(P4)