# defaultdict 초기값을 리스트 형태로 만들기
from collections import defaultdict

if __name__ == "__main__":
    li = [("yellow", 1), ("blue", 2), ("green", 3), ("blue", 4), ("red", 1)]
    dic = defaultdict(list)
    for k, v in li:
        dic[k].append(v)

    print(dic)
    print(dic.items())