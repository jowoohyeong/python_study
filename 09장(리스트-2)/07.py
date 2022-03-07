# 일반적인 리스트 연산 실습

nums = [1, 5, -9, 100]
min = nums[0]
max = nums[0]

for i in range(1, len(nums)):
    if min > nums[i]:   # 최소값
        min = nums[i]
    if max < nums[i]:   # 최대값
        max = nums[i]

print(min, max)

# 믄자열에서 가장 짧은 문자열 구하는 알고리즘
words = "bird dog cat horse lion tiger elephant bow".split()
words_han = "안녕 하이 가지마세요 반갑습니다 가세요 오랜만입니다".split()
sword = words[0]
s_list = [words[0]]
l_word = words[0]
for i in range(1, len(words)):
    if len(sword) >= len(words[i]):
        if len(sword) > len(words[i]):
            s_list.clear()
            s_list.append(words[i])
            sword = words[i]
        else:
            s_list.append(words[i])
            sword = words[i]
    if len(l_word) < len(words[i]):
        l_word = words[i]

print("가장 짧은 단어: ", sword)
print("가장 짧은 단어들: ", s_list)
print("가장 긴 단어: ", l_word)
