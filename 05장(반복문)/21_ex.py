# 반복문으로 문자열 관련 처리하기 실습
fruit = "apple"
for letter in fruit:
    print(letter,end=" ")
print("---------")

s= input("문자열 입력(영문자): ")
result = ""
for ch in s:
    if ch not in "aeiouAEIOU":
        result += ch
print("모음제거: " + result)

print("---------")

# 문자열 입력, 자음과 모음 개수
word = input("문자열 입력(영문자): ")
word = word.lower()
vowels = 0
consonants = 0
if len(word) > 0 and word.isalpha():
    for ch in word:
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1
print("모음: {}, 자음 : {}".format(vowels, consonants))
