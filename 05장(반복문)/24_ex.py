# 입력받은 문자열의 공백을 제거

word = input("문자열 입력: ")

result = ""
for ch in word:
    if not ch.isspace():
        result += ch

print("공백을 제거한 문자열: " + result)