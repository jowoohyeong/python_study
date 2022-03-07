# 파일의 단어 개수 출력

f = open("words.txt", mode="r", encoding='utf-8')
dic = {}
for line in f.readlines():
    li = line.split()
    for key in li:
        print(key)
        if key in dic:
            dic[key] += 1
        else:
            dic[key] = 1
print(dic)
f.close()

