# 몸무게와 키를 입력받아 BMI 20.0이상이고 25미만이면 표준
# 아니면 체중관리 필요

height = float(input("키(cm) 입력: "))
weight = float(input("몸무게(kg) 입력: "))

height /= 100
BMI = weight / (height * height)

print("당신의 BMI는 ", BMI, "입니다.")
if (20.0 <= BMI) and (BMI < 25.0):
    print("표준입니다.")
else:
    print("체중관리 필요")