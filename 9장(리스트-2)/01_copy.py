# 얕은 복사 shallow copy : 주소 값 복사, 원본 리스트에 영향 끼침
scores = [10,20,30,40,50]
value = scores
print("score 주소: ", id(scores))
print("value 주소: ", id(value))
value[3] = 13
value.append(-70)
value.insert(1, -100)
print("scores: ", scores)
print("value: ", value)