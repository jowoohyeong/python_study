# 문자열입력 
# 알파벳문자 개수, 숫자의 개수, 스페이스의 개수 출력


word = input("문자열 입력(영문자): ")
str = 0
su = 0
space = 0
etc = 0
for ch in word:
    if ch.isalpha():
        str += 1
    elif ch.isdigit():
        su += 1
    elif ch.isspace():
        space += 1
    else:
        etc += 1

print("알파벳 : {}, 숫자: {}, 스페이스: {}, 기타: {}".format(str, su, space, etc))