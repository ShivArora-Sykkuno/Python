
for _ in range(int(input())):
    N = int(input())
    arr = sorted(list(map(int, input().split())))
    diff = 10**30
    for i in range(N-1):
        if arr[i+1] - arr[i] < diff:
            diff = arr[i+1] - arr[i]
    print(diff)
