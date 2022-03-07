# 순서를 따지는 dictionary 객체
# 일반적인 딕셔너리는 순서를 보장하지 않는다./ 인덱스가 없기 때문
dic = {}
dic["a"] = 100
dic["b"] = 200
dic["c"] = 300
dic["d"] = 400
dic["e"] = 500

for k,v in dic.items():
    print(k, v)

# 딕셔너리의 순서와 동등성 비교를 개선한 모듈
from collections import OrderedDict
dic2 = OrderedDict(dic)
print(dic2)