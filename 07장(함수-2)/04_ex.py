# mutable object, dictionary 타입
# 딕셔너리의 키 값은 유니크해야하고 값은 변경 가능하다.
# 딕셔너리 call by reference 가 성립되는 이유는 mutable object 이기 때문
# call by objective-reference 라고 칭함
dic = {"name": "woo hyoeng", "age": 25, "height": 165}
dic2 = {"name": "woo hyoeng", "name": 25, "height": 165}

print(dic)
print(dic2)

print("dic[name] :", dic["name"])

def change(d):
    print("함수 내부 연산 전 : ", d, id(d))
    d["weight"] = 70
    print("함수 내부 연산 후 : ", d, id(d))


print("함수 호출 전: ", dic, id(dic))
change(dic)
print("함수 호출 후: ", dic, id(dic))
