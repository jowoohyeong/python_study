# 2차원 리스트 실습
double_list = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15]
]
print(double_list)
print(double_list[0])
print(double_list[1])
print(double_list[2])

print(id(double_list))
print(id(double_list[0]))
print(id(double_list[1]))
print(id(double_list[2]))

for i in range(len(double_list)):
    for j in range(len(double_list[i])):
        print(double_list[i][j], end="\t")
    print()

rows = 5
cols = 6
db_list = []
# for row in range(rows):
#     db_list += [[0] * cols]
db_list = [[0] * cols for row in range(rows)]
print(db_list)

li1 = [1,2,3]
li1[0] = 10
print(li1)

li2 = [[1,2],[3,4]]
li2[0][1] = -7
print(li2)
hap = 0
for i in range(len(double_list[0])):
    hap += double_list[0][i]
print("hap: ", hap)

hap = 0
for i in range(len(double_list)):
    for j in range(len(double_list[i])):
        hap += double_list[i][j]
print("hap: ", hap)