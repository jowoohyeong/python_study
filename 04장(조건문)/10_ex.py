# 쇼핑몰에서 물건 구매시 구입액 5만원 이상이면 5%할인
# 사용자에게 구입 금액 입력, 최종 할인금액과 지불 금액 출력

money = int(input("구입 금액 입력:"))

if money >= 50000:
    disCount = money * 0.05
    print("구입 금액: ", money, "원")
    print("할인 금액: " + str(disCount) + "원")
    print("최종 지불 금액: " + str(money-disCount) + "원")
else:
    print("할인이 없다.")
    print("최종 금액 : " + str(money))