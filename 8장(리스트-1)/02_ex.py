# 학성 성적 처리 프로그램

STUDENT = 5
scores= []
sum = 0
cnt = 0
for i in range(STUDENT):
    score = int(input("성적을 입력하세요: "))
    scores.append(score)
    sum += score
    if score >= 80:
        cnt += 1

ave = float(sum / STUDENT)

print("성적 평균은 %.2f입니다." % ave)

print("80점 이상 성적을 받은 학생은 %d명입니다." % cnt)