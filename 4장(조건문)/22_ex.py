# 사용자로부터 월 입력받아 일수 구하기

month = int(input("월 입력:"))

if month == 2:
    print("28일")
elif month ==1 or month ==3 or month == 5 or month == 7 or month == 8 or month == 10 or month ==12:
    print("31일")
else :
    print("30일")