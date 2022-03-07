# 일회용 패스워드 생성기를 이용
# 3개의 패스워드 생성하여 출력
# 난수 발생 문자열 :
from random import *

def get_password():
    temp = "0123456789"
    password = ""
    for i in range(6):
        index = randint(0,9)
        password += temp[index]

    return password

print(get_password())
print(get_password())
print(get_password())
