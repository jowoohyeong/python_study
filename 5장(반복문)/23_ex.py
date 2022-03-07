# 전화번호 입력
# "-" 제거

phone = input("전화번호 입력(***-****-****): ")

_phone = ""
plen = len(phone)
if plen == 12 or plen == 13:
    for num in phone:
        if num != "-":
            _phone += num
else:
    print("잘못된 전화번호")
print(_phone)