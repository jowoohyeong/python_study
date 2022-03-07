itemPrice = int(input("물건값입력: "))

_1000 = int(input("1000원 개수: "))
_500 = int(input("500원 개수: "))
_100 = int(input("100원 개수: "))

nod_money = _1000*1000 + _500*500 + (_100*100) - itemPrice
print("거스름돈: ", nod_money)

n_1000 = nod_money // 1000
nod_money = nod_money % 1000

n_500 = nod_money // 500
nod_money = nod_money % 500

n_100 = nod_money // 100
nod_money = nod_money % 100

n_1 = nod_money // 1
nod_money = nod_money % 1

print("n_1000: ",n_1000, ", n_500: ", n_500, ", n_100: ",n_100, ", n_1: ", n_1)


