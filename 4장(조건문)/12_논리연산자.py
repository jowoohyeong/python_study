# logical operator는 두 개 이상의 조건을 조합해서 참 거짓을 계산할 대 사용하는 연산자
# and(논리곱), or(논리합), not(논리부정)

name = "조우형"
age = 20
height = 160

# and 논리 연산자는 첫 조건이 거짓이면 이후 조건은 검사하지 않는다.(단축계산)
if age >= 21 and height >= 160 and name == "조우형":
    print(name + "님은 놀이기구 탑승 가능")
else:
    print(name + "님은 놀이기구 탑승 가능불가")

if not(1 == 1):
    print("참이다.")
else:
    print("거짓이다.")