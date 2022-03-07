# 정렬 실습
list1 = [4,8,9,-1,10]
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)

# 선택 정렬 알고리즘을 통한 정렬
def selectionSort(aList):
    for i in range(len(aList)-1):
        leastNum = aList[i]
        for j in range(i+1, len(aList)):
            if leastNum > aList[j]:
                idx = j
                leastNum = aList[j]
        if leastNum != aList[i]:
            aList[i], aList[idx] = aList[idx], aList[i]

# 버블 정렬
def bubbleSort(aList):
    for i in range(len(aList)-1):
        for j in range(len(aList)-i-1):
            if aList[j] > aList[j+1]:
                aList[j], aList[j+1] = aList[j+1], aList[j]


list1 = [7, 9, 5, 1, 8, -1, 2, -4, 3, -34]
selectionSort(list1)
print(list1)
print("------------------------------------")
list1 = [7, 9, 5, 1, 8, -1, 2, -4, 3, -34]
bubbleSort(list1)
print(list1)