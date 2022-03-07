# 영한 사전 만들기

d1 = {"one": "하나", "two": "둘", "three":"셋"}

print("종료 시 -1 입력하세요")
while True:
    word = input("단어를 입력: ")
    if word in d1:
        print(word,"단어의 뜻: ", d1.get(word))
    elif word == "-1":
        print("종료")
        break
    else:
        print("해당하는 단어가 없습니다.")