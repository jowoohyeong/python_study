# 순서를 따지는 dictionary 객체
# 일반 딕셔너리를 정렬하여 OrderedDict로 포장하기
dic = {}
dic["a"] = 100
dic["b"] = 200
dic["z"] = 300
dic["d"] = 400
dic["r"] = 500
dic["v"] = 600
dic["h"] = 700
dic["y"] = 800
dic["m"] = 500

# 키 값 정렬
li1 = sorted(dic.keys())
li2 = sorted(dic.values())
print(li1)
print(li2)
print(dic["z"])
print("----------------------")
from collections import OrderedDict
def sort_by_key(t):
    return t[0]

dic1 = OrderedDict(dic)
print(dic1)
print(type(dic1))
li3 = sorted(dic1.items(), key=sort_by_key)
print(type(li3))

print(li3)

for k, v in OrderedDict(li3).items():
    print(k, v)

# 동등성 비교 / 논리적 동등
# 주소는 다르지만 요소들의 값이 순서가 비록 틀리더라도 논리적 동등으로 바라보는 시점
# 일반적인 딕셔너리의 동등성 비교
dic1 = {"가": 1, "나":2, "다":3}
dic2 = {"가": 1, "다":3, "나":2}
print(dic1 == dic2)

# OrderedDict는 두 개의 OrderedDict를 비교할 때 해당하는 값의 순서와 해당하는 키, 값이 같아야지만 동등하게 바라본다
# 일반적인 딕셔너리보다 깐깐하다
from collections import OrderedDict
dic3 = OrderedDict(dic1)
dic4 = OrderedDict(dic2)
dic5 = OrderedDict(dic1)
print("dic3 주소: ", id(dic3))
print("dic5 주소: ", id(dic5))
print(dic3 == dic4)
print(dic3 == dic5)

# 결론
# OrderedDict모듈은 딕셔너리의 순서대로 저장하지 않는 방식을 순서대로 저장하는 방식으로 개선됨
# 딕셔너리의 동등성 비교에서 일반적인 딕셔너리는 순서를 유지하지 않아도 해당 키 값이 동등하다면 True
# OrderedDict에서는 순서와 키 값이 무조건 같아야 True
# OrderedDict를 사용하면 정확한 데이터의 순서나 값을 유지하는데 일반 딕셔너리에 비해서는 엄청 좋은 면이 존재한다.
# 웬만하면 OrderedDict 사용 권장?