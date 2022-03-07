# 사용자 초등학생, 중학생, 고등학생, 대학생 분류

year = int(input("태어난 연도 입력: "))
age = 2022 - year + 1
print(age)

if (8 <= age) and (age <= 13):
    print("초등학생")
elif (14 <= age) and (age <= 16):
    print("중학생")
elif (17 <= age) and (age <= 19):
    print("고등학생")
elif (20 <= age) and (age <= 27):
    print("대학생")
else:
    print("일반인입니다.")