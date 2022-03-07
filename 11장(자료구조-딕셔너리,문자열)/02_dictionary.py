# 순회 방법
s = {"국어": 80, "수학":95, "영어":80}

# 키 값 출력 루프
print(s.keys(), ",  type:\t", type(s.keys()))
for subject in s.keys():  #s.keys()
    print(subject, end=" ")
print("")
print("--------------------")

# 값 출력
print(s.values(), ",  type:\t", type(s.values()))
for subject in s.values():  #s.keys()
    print(subject, end=" ")
print("")
print("--------------------")

print(s.items(), ",  type:\t", type(s.items()))
for subject in s.items():
    print(subject, end=" ")
print()
print("--------------------")
# 함축
d1 = {x: x*x*x for x in range(5)}
print(type(d1))
print(d1)
print("--------------------")
# 정렬, 파이썬의 딕셔너리는 근복적으로 요소의 순서가 없기 때문에 순서대로 저장하지 않음
d2 = {"pens":6, "bags": 1, "books": 5,"bottles":4,"coins":3, "cups":2}
print(d2)
# 딕셔너리 리스트로 변환
print(list(d2))
# 키 값으로 정렬 -> sorted
print("keys 정렬:\t", sorted(d2))
print("values 정렬:\t", sorted(d2.values()))

# 딕셔너리의 값에 따라 키 값을 정렬
print("value 값에 따라 정렬: ", sorted(d2, key=d2.__getitem__))

print("--------------------")
d1 = {1:"23",2:"1231",6:"조우형", 8:"감", 10:"파이썬", 5:"소나무", 4:"김철수"}
d2 = {1:23,2:1231,6:32, 8:15, 10:3, 5:5, 4:6}

print(sorted(d1.items()))
print(sorted(d2.items()))