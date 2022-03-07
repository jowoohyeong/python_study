# 2차원 리스트 체커보드 실습

def printList(li):
    for i in range(len(li)):
        for j in range(len(li)):
            print(li[i][j], end=" ")
        print("")


def init(li):
    for i in range(len(li)):
        for j in range(len(li)):
            if (i + j) % 2 == 0:
                li[i][j] = 1


if __name__ == "__main__":
    table = [[0] * 5 for i in range(5)]
    init(table)
    printList(table)
