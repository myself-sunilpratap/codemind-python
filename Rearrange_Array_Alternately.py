n = int(input())
for i in range(n):
    a = int(input())
    arr = list(map(int, input().split()))
    left = 0
    right = a - 1
    max_val = arr[right] + 1 
    for i in range(a):
        if i % 2 == 0:
            arr[i] += (arr[right] % max_val) * max_val
            right -= 1
        else:
            arr[i] += (arr[left] % max_val) * max_val
            left += 1
    for i in range(a):
        arr[i] = arr[i] // max_val
    print(*arr)