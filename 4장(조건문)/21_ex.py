# 1. 사용자 점수 입력
# 2. 점수 95 이상 100이하 A+
# 4. 90이상 94 이하 A0-

score = int(input("성적입력: "))

if score >= 90:
    if score < 95:
        print("A0")
    else:
        print("A+")
elif score >= 80:
    if score < 85:
        print("B0")
    else:
        print("B+")
elif score >= 70:
    if score < 75:
        print("C0")
    else:
        print("C+")
elif score >= 60:
    if score < 65:
        print("D0")
    else:
        print("D+")
else:
    print("F!")