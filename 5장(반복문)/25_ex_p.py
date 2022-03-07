# 입력받은 문자열 거꾸로 출력

word = input("문자열 입력: ")
wordLen = len(word)
result = ""
for ch in word:
    result = ch + result

print("문자열 거꾸로 출력: " + result)

s_list = list(word)
print("s_list: ", s_list)
# reverse 함수는 리스트만 역순으로 출력
s_list.reverse()
print("".join(s_list))

s1 = word
# reversed 함수는 문자열만 역순으로 출력
print("".join(reversed(s1)))

# 문자열[[a]::b] => [a] 생략가능 , a번째 문자열부터 출력, b 음수일때 역순
print(word[::-1])
print(word[3::-1])