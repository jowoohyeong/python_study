# 변수의  두 개의 값을 서로 바꾸는 예제
num1 = 100
num2 = 200
print(type(num1))
print("num1 : ", num1, ", num2: ", num2)
temp = num1
num1= num2
num2= temp
print("num1 : ", num1, ", num2: ", num2)