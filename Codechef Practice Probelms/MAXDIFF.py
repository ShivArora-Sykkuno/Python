for _ in range(int(input())):
    N, K = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    if K <= N // 2:
        print(abs(sum(arr[:K]) - sum(arr[K:])))
    else:
        print(abs(sum(arr[:N-K]) - sum(arr[N-K:])))
