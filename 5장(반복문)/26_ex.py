# 문자열 왼쪽 공백만 삭제

statements = "     안   녕 ! !      "
print("제거전 문자열: " + statements)
print("왼쪽 공백 제거: " + statements.lstrip())
print("오른쪽 공백 제거: " + statements.rstrip())
print("양쪽 공백 제거: " + statements.strip())

# 중간공백은 24_ex!!!

# 문자열 나누기
word = "현재 1월 입니다."
print(word.split())