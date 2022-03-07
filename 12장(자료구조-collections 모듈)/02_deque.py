# deque vs list
from collections import deque
import time

n = 5000000
deque_list = deque()
list = list()

start = time.time()
for i in range(n):
    deque_list.insert(1, i)
end = time.time()
print("deque append time: ", end - start)

start = time.time()
for i in range(100000):
    list.insert(1, i)
end = time.time()
print("list append time: ", end - start)
print("-------------추출-----------------")
# start = time.time()
# for i in range(n):
#     deque_list.pop()
# end = time.time()
# print("deque append time: ", end - start)
#
# start = time.time()
# for i in range(n):
#     list.pop()
# end = time.time()
# print("list append time: ", end - start)

print("-------------뒤 추출-----------------")
start = time.time()
for i in range(n):
    deque_list.popleft()
end = time.time()
print("deque append time: ", end - start)

start = time.time()
for i in range(1000):
    list.pop(0)
end = time.time()
print("list append time: ", end - start)


# 데이터 추가 제거할 때 deque가 훨씬 좋은 성능을 보여준다.
# 대용량일수록 더욱더 많은 차이를 나타낸다