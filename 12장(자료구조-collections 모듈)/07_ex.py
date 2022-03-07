# 각 알파벳의 글자의 수를 세어 딕서너리 리턴하기
from collections import defaultdict

def counterWords(words):
    counter = defaultdict(list)
    for word in words:
        length = len(word)
        counter[length].append(word)
    return counter




if __name__ == "__main__":
    li = "감자 귤 사과 배 오징어 꼼장어 불가사리".split()

    result = counterWords(li)
    print(result)