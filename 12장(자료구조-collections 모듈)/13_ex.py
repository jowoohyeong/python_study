# 텍스트 마이닝 기법
def file_read(text):
    f = open("./law.txt", mode="r", encoding="utf-8")
    for line in f.readlines():
        splited_line = line.split()
        print(splited_line)
        text.extend(splited_line)

    f.close()

if __name__ == "__main__":
    from collections import defaultdict
    from collections import OrderedDict
    text = []
    file_read(text)
    word_count = defaultdict(lambda : 0)
    for word in text:
        word_count[word] += 1
    for k, v in OrderedDict(sorted(word_count.items(), key=lambda x: x[1], reverse=True)).items():
        if v > 1:
            print(k, v)
