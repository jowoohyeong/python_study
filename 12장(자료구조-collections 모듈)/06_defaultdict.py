# 함수를 통해 딕셔너리 초기화
# 일반 딕셔너리는 초기화
from collections import defaultdict

def countLetters(word):
    counter = {}
    for letter in word:
        if letter not in counter:
            counter[letter] = 0
    return counter

# setdefault
def setD(word):
    counter = {}
    for letter in word:
        counter.setdefault(letter, 0)
    return counter

# defaultdict 모듈
def deD(word):
    counter = defaultdict(lambda: 0)
    for letter in word:
        counter[letter] += 1
    return counter


if __name__ =="__main__":
    dic = countLetters("가나다라마바")
    print("dic: ", dic.items())
    dic2 = setD("가나다라마바")
    print("dic2: ", dic2.items())
    dic3 = deD("가나다라마바")
    print("dic3: ", dic3.items())

