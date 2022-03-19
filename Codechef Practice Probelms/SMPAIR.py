for _ in range(int(input())):
    x = int(input())
    arr = sorted(list(map(int, input().split())))
    res = arr[0] + arr[1]

    print(res)
