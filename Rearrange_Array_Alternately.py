T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    left = 0
    right = N - 1
    max_val = arr[right] + 1 
    for _ in range(N):
        if _ % 2 == 0:
            arr[_] += (arr[right] % max_val) * max_val
            right -= 1
        else:
            arr[_] += (arr[left] % max_val) * max_val
            left += 1
    for _ in range(N):
        arr[_] = arr[_] // max_val
    print(*arr)