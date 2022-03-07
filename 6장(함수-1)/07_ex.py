# 리턴값없는 함수

def printInfo(name, age):
    print("===================")
    print("이름 : ", name)
    print("이름 : ", age)
    print("===================")
    return

print("이름과 나이를 입력(종료: q) : ")
while True:
    name = input("회원명을 입력: ")
    age = int(input("나이 입력: "))
    printInfo(name, age)

    q = input("계속 입력(y or n)?: ")
    if q == "n":
        break
    
