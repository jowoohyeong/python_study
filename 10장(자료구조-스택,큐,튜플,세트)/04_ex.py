# 큐 함수 만들기

def offer(data, n):
    data.append(n)

def poll(data):
    if len(data) > 0:
        data.pop(0)
    return False

def offer_data(data):
    for i in range(5):
        offer(data, i)
        print("현재 큐: ", data)

def poll_data(data):
    for i in range(6):
        poll(data)
        if i >= 5:
            print("빈 큐")
            return
        print("현재 큐: ", data)

if __name__ == "__main__":
    queue = []
    offer_data(queue)
    poll_data(queue)
