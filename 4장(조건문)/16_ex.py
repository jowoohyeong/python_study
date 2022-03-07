# 중첩(nested) if ~ else

appleQua = input("사과의 상태입력(좋음, 나쁨): ")
applePrice = int(input("사과 1개당 가격: "))

if appleQua == "좋음":
    if applePrice < 1000:
        print("10개구입")
    else:
        print("5개구입")
else:
    print("사과 구입안함")
