# 부분 집합 연산
s1 = {10,20,30}
s2 = {10,20,30}
print("s1 == s2 : ", s1 == s2)
print("s1 != s2 : ", s1 != s2)

# 부등호 연산을 통해 부분집합 확인
# 진상위 집합의 개념 : b가 a에 포함되지만 서로 집합은 동일하지 않는 집합
s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3}

# 연산자
print("s2는 s1의 부분집합인가? ", s2 < s1)

# issubset() - 부분집합, issuperset() - 상위집합  // 상위집합은 부등호로 확인 불가
print("s2는 s1의 부분집합인가? ", s2.issubset(s1))
print("s1는 s2의 상위집합인가? ", s1.issuperset(s2))

sets = set("Hello_h")
print(sets)

if "H" in sets:
    print("'H'가 포함되어있다")

# 집합연산
print("--------------------")
s1 = {1, 2, 3, 4, 5, 6}
s2 = {1, 2, 3}
print("합집합: ", s1 | s2)
print("합집합: ", s1.union(s2),", ", s2.union(s1))

print("교집합: ", s1 & s2)
print("교집합: ", s1.intersection(s2),", ", s2.intersection(s1))

print("차집합: ", s1 - s2)
print("차집합: ", s1.difference(s2))
print("차집합: ", s2.difference(s1))

# all() 모든 요소 값이 참이여야 True 리턴
s1 = {10,20,30,40,50,60}
s2 = {0,0,0,0,0, 49}
print("s1 all()결과 : ", all(s1))
print("s2 all()결과 : ", all(s2))

# any() 모든 요소 값이 참이여야 True 리턴
print("s1 any()결과 : ", any(s1))
print("s2 any()결과 : ", any(s2))

# 같은 요소가 없는 집합 확인
print("같은 요소가 없는가? ", s1.isdisjoint(s2))

# pop() 집합요소 제거시 임의의 요소 제거
for _ in range(len(s1)):
    print(s1.pop(), end=" ")
print()
print(len(s1))

a = {1,2,3}
b = {3,4,5}