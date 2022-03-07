# 중복 (nested) if ~ else
# 아이디 입력받고 등록된 아이디인지 검사
# 아이디 존재시 비밀번호 입력
# 패스워드는 "1234" 로 고정


userList = ["qq", "aa", "ee"]
pw = "1234"

id = input("아이디 입력: ")

if id in userList:
    password = input("비밀번호 입력: ")
    if password == pw:
        print(id + " 로그인")
    else:
        print("비밀번호 오류")
else:
    print("로그인 실패")