# 문제
# 머리 글자어 acronym 구하기

def main():
    string = input("문자열 입력: ")
    li = string.upper().split()
    result = ""
    for word in li:
        result += word[0]

    print(result)

if __name__ == "__main__":
    main()