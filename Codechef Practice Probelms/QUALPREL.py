




for _ in range(int(input())):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    count = K
    for i in range(K - 1, N - 1):
        if arr[i] == arr[i + 1]:
            count += 1
        else:
            break
    print(count)
