# 학생의 성적 출력 실습

dt = [(90, 80), (85, 75), (90, 100)]

for i, score in enumerate(dt):
    sum = score[0] + score[1]
    ave = sum / len(score)
    print(i+1, "번째 학생의 총점은 ", sum, "점이고, 평균은 ", ave, "입니다.")