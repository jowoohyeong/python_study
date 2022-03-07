# collections 모듈이란 기존에 배웠던 자료구조(리스트, 큐, 튜플, 딕셔너리)를 좀 더 확장하여 제작된 파있너의 내장모듈
# 1) deque (double-ended queue)모듈은 스택과 큐를 모두 지원하는 모듈
# 양방향 데이터 입출력 자료구조

from collections import deque
deque_list = deque()
print(deque_list)

for i in range(5):
    deque_list.append(i)
print(deque_list)

# 요소 삭제  pop(0) 불가
# 스택과 동일하게 pop() 함수 지원
print(deque_list.pop())

# appendleft() 사용   // 왼쪽에 요소 삽입
deque_list.clear()
for i in range(5):
    deque_list.appendleft(i)
print(deque_list)

# 원형 연결리스트(Linked List)의 특성을 지원한다.
# 연결 리스트는 데이터를 저장할 때, 요소의 값을 한 쪽으로 연결한 후, 요소의 다음 값의 주소값을 저장하여 연결하는 기법

# rotate(n) : 요소를 n 만큼 회전하는 메소드
deque_list.rotate(2)
print(deque_list)
deque_list.rotate(-1)
print(deque_list)
print("-----------------------")
# reversed()    / 기존 요소를 역순으로
print(deque(reversed(deque_list)))

# extend()  : 리스트를 우측에 삽입
# extendleft() : 리스트를 좌측에 삽입
print("-----------------------")
deque_list.extend([5,6,7])
print(deque_list)
deque_list.extendleft([5,6,7])
print(deque_list)
print("-----------------------")
deque_list.clear()
base = ["a","b","c","d","e"]

# maxlen 매개변수는 deque의 사이즈를 고정하는 인자값
deque_list = deque(base, maxlen= 3)
print(deque_list)
# popleft() 메소드는 deque 에서 왼쪽의 요소를 삭제
print(deque_list.popleft())
print(deque_list)

