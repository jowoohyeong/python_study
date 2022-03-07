# 성적 처리 프로그램

score = [
    [100, 100, 100],
    [20,20,20],
    [30,30,30],
    [40,40,40],
    [50,50,50]
]

print("번호\t국어\t영어\t수학\t총점\t평균")
print("------------------------------------------------")
haps = [0 for i in range(len(score[0]))]
total = 0
avetotal = 0.00
for i in range(len(score)):
    print(" ", i+1,end="\t\t")
    hap = 0
    ave = 0.00
    for j in range(len(score[i])):
        print(score[i][j], end="\t\t")
        hap += score[i][j]
        haps[j] += score[i][j]
    ave = hap/len(score[i])
    print("%d\t\t%.2f" % (hap, ave))
    avetotal += ave
    total += hap
print("------------------------------------------------")
print("총점", end="\t")
for i in range(len(haps)):
    print(haps[i], end="\t\t")
print("%d\t\t%.2f" % (total, avetotal))