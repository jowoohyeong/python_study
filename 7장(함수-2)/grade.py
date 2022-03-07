# grade 모듈 만들기

# 성적 입력받기, 음수시 종료
def readList():
    sc_list = []
    flag = True

    while flag:
        score = int(input("성적 입력(종료:음수): "))
        if score < 0:
            flag = False
        else:
            sc_list.append(score)
    return sc_list

# 성적 정렬
def sortingList(li):
    li.sort()
    return li

# 성적 출력
def showScore(li):
    j = 0
    for i in li:
        print((j+1), "번째 성적 출력 ", i)
        j += 1