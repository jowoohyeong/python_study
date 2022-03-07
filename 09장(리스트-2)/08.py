# 탐색하기
#
# list_word = "gold blue red yellow green".split()
# s = input("찾고자 하는 단어 입력: ")
#
# if s in list_word:
#     index = list_word.index(s)
#     print(index, "에 존재")
# else:
#     print("없다")

def number_search(arr, key):
    cnt = 0
    for i in range(len(arr)):
        if arr[i] == key:
            cnt += 1

    if cnt == 0:
        return 0
    else:
        return cnt


find_num = 23
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 1]
print("리스트안에 있는", find_num, "의 개수: ", number_search(num_list, find_num))

# 모든 조건에 만족하는 항목 전부 찾기
result =[]
for i in num_list:
    if i >= 5:
        result.append(i)
print(result)