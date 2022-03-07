# 부울(bool) 변수 알아보기
# 부울변수는 플래그 변수 형태로 주로 사용
# 파이썬은 대문자로 시작하는 True, False 로 사용

flag = True
print(type(flag))
print(flag)

flag = not flag
print(flag)

if flag:
    print("참입니다.")
else:
    print("거짓입니다.")
    flag = not flag

if flag:
    print("참입니다.")
else:
    print("거짓입니다.")