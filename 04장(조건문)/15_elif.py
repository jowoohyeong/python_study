# if ~ elif ~ else


score = int(input("성적입력: "))

if score >= 90:
    print("점수가 90점이상, A")
elif score >= 80:
    print("점수가 80점이상, B")
elif score >= 70:
    print("점수가 70점이상, C")
elif score >= 60:
    print("점수가 60점이상, D")
else:
    print("F!")