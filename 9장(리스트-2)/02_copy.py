# 깊은 복사 deep copy : 새로운 리스트 객체 생성, 기존 리스트 영향 X

# list()
scores = [10, 20, 30, 40, 50]
value = list(scores)
print("score 주소: ", id(scores))
print("value 주소: ", id(value))
value[3] = 13
value.append(-70)
value.insert(1, -100)
print("scores: ", scores)
print("value: ", value)

print("_-------------------------")

# deepcopy, copy
import copy
item1 = [1, 2, 3, 4, 5, -3]
item2 = copy.deepcopy(item1)
# item2 = copy.copy(item1)
print("item1 주소: ", id(item1))
print("item2 주소: ", id(item2))
item2[3] = 13
item2.append(-70)
item2.insert(1, -100)
print("item1: ", item1)
print("item2: ", item2)

# [:]
index1 = [1, 2, 3, 4, 5, -3]
index2 = index1[:]
print("index1 주소: ", id(index1))
print("index2 주소: ", id(index2))
index2[3] = 13
index2.append(-70)
index2.insert(1, -100)
print("index1: ", index1)
print("index2: ", index2)