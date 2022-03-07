# 항공사 짐 -> 20kg 이상 2만원 추가비용
# 20kg 미만은 수수료 없다.

weight = int(input("짐의 무게: "))
if weight >= 20:
    print("2만원 추가비용 있다.")
else:
    print("수수료없다.")
print("감사합니다.고객님")