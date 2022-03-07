# 별찍기
for i in range(5):
    print("{:>5}".format("*" * (i+1)), end="")
    print("*" * i, )
print("--------------------")
for i in range(1, 6):
    for j in range(5-i):
        print(" ", end="")
    for k in range(1, i*2):
        print("*", end="")
    print("")

# format 중앙정렬 !
for i in range(1, 11, 2):
    print("{:^10}".format("*" * i))

# reverse
# *********
#  *******
#   *****
#    ***
#     *
for i in range(5):
    for j in range(i):
        print(" ", end="")
    for k in range(10,(i*2)+1, -1):
        print("*", end="")

    print("")
print("-----------")
for i in range(9, 0, -2):
    print("{:^10}".format("*" * i))