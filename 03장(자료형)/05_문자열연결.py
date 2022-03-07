# 문자열의 연결
first_name = "woohyeong"
last_name = "Jo "
name = last_name + first_name
print(name)

# 파이썬에서는 모든 데이터가 데이터 타입이 존재한다.
# 타입이 일치하지 않으면 + 연산자 사용 불가!
print("Person" + str(100))
print("->" * 10)

# 형식지정자(%s)
price = 10000
message = "hello world"
text = "값은 %s이다."
text2 = "\"%s\"와 \"%s\""

print(text % price)
print(text % message)
print(text2 %(price, message))