# 자료구조: 데이터의 특징을 고려하여 데이터를 저장하는 방법
# 특징 : 최대한 메모리를 효율적으로 저장 및 반환, 데이터를 관리, 대용량일수록 빨리 저장 및 검색
# 메모리를 효율적으로 사용하면 유저들에게 실행결과를 빨리 돌려주는 방법

# 스택 : LIFO, Last In First Out
# 저장 push 추출 pop
stack_data = []
stack_data.append(10)
stack_data.append(20)
stack_data.append(30)
stack_data.append(40)
stack_data.append(50)
print(stack_data)
print(stack_data.pop())
print(stack_data)

# 입력받은 텍스트 역순 추출 프로그램
# word = input("텍스트 입력: ")
word = "Hello world, python"
li = list(word)
result = []
for _ in range(len(li)):
    result.append(li.pop())

print(result)
print(word[::-1])
