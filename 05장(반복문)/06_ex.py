# 피보나치 수열

n = int(input("정수 입력: "))

# 내 풀이
arr = [1, 1]
for i in range(2, n+1):
    arr.append(arr[i-1]+arr[i-2])
    if arr[i] > n:
        break

print(arr)

n1 = 1
n2 = 1
n3 = 1
for i in range(1, n):
    if i < 3:
        n3 =1
    else:
        n3 = n1 + n2
        n1 = n2
        n2 = n3

    if n3 < n:
        print(n3, end=" ")