# 텍스트 파일에 사용된 단어 개수 출력
# 단어에서 마침표 제거, 대문자 -> 소문자 변환
def process(li):

    str_list = []
    for word in li:
        str = ""
        for ch in word:
            if ch.isalpha():
                str += ch
        str_list.append(str.lower())
    return str_list
if __name__ == "__main__":
    f = open('./words.txt', mode="r")
    text = set()
    for i in f.readlines():
        str_list = i.split()
        text.update(process(str_list))
    print(text)
    print("사용한 단어의 개수: ", len(text))
    f.close()
