# 문자열 입력받기
# 문자, 숫자, 공백 개수 출력 프로그램

def main():
    string = input("문자열을 입력: ")
    # string = "A picure is worth a thousand words."
    dic = {"space": 0, "digits": 0, "alpha": 0, "etc": 0}
    for ch in string:
        if ch.isspace():
            dic["space"] += 1
        elif ch.isalpha():
            dic["alpha"] += 1
        elif ch.isdigit():
            dic["digits"] += 1
        else:
            dic["etc"] += 1
    print(dic)

if __name__ == "__main__":
    main()
