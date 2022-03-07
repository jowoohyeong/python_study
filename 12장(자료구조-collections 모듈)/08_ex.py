# 각 알파벳의 글자의 수를 세어 딕서너리 리턴하기
from collections import defaultdict

def counterWords(words):
    counter = defaultdict(set)
    for word in words:
        length = len(word)
        counter[length].add(word)
    return counter


if __name__ == "__main__":
    li = "한국 미국 우즈베키스탄 사우디아라비아 스페인".split()
    li = set(li)
    result = counterWords(li)
    print(result)