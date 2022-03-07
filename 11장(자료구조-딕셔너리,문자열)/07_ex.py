# 회문 ex) mom, civic, dad

def check(word):
    for i in range(len(word)//2):
        if word[i] != word[-(i+1)]:
            return False
    return True

if __name__ == "__main__":
    word = input("문자열 입력: ")
    word = word.replace(" ", "")
    flag = check(word)
    if flag: print("회문입니다.")
    else: print("회문이 아니다")


