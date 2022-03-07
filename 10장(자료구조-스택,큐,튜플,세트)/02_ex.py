def push(data, n):
    data.append(n)

def pop(data):
    if len(data) > 0:
        return data.pop()
    return False
def push_data(data):
    for i in range(5):
        push(data, i)
        print("현재 스택:", data)
def pop_data(data):
    for i in range(6):
        pop(data)
        if i >=5:
            print("빈 스택")
            return
        print("현재 스택:", data)

if __name__ == "__main__":
    stack = []
    push_data(stack)
    pop_data(stack)