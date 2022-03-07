# 대학 졸업요건 140학점 이상 이수, 평점 최소 2.0
# 이수학점과 평점 입력

total = int(input("이수학점 입력: "))
grade = float(input("평점 입력: "))

if total >= 140 and grade >= 2.0:
    print("졸업가능")
else:
    print("졸업불가")