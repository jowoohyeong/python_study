# defaultdict 모듈은 딕셔너리 요소 생성 시, 키의 기본 값을 지정하는 방법
# 일반 딕셔너리는 key 값으로 value 값을 알아낼 수 있다.


from collections import defaultdict

# defaultdict의 아직 모르는 모든 키에 대해 기본 key 값을 0으로 정함
d = defaultdict(lambda : 0)
print(d['a'])
print(d.get('b'))
print("--------------")
d.clear()
# key -> int , float, str, list, set 가능
d = defaultdict(int)
print(d['a'])
print(d[100])




li = [2,4]
li.extend([1,2,3,4])
print(li)