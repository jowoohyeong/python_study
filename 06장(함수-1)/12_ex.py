# 10진수 입력받기
# 2진수 문자열로 변환

decn = int(input("십진수 입력: "))

def decTobin(num):
    bin = ""
    while num != 0:
        value = num % 2
        if value == 0:
            bin = "0" + bin
        else:
            bin = "1" + bin
        num //= 2
    return bin

print(decTobin(decn))
print("-----------------------")
# 파이썬에서 제공하는 진법 변환 함수
print("2진수: ", bin(decn))
print("8진수: ", oct(decn))
print("16진수: ", hex(decn))

# 2진수의 값을 10진수로 변환
print(int("0b1010", 2))
print(int("0o12", 8))
print(int("0xa", 16))