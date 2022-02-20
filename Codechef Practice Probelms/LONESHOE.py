for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    res = dict()
    for i in arr:
        if res.has_key(i):
            res[i] += 1
        else:
            res[i] = 1
    for k, v in res.items():
        if v == 1:
            print(k, end=" ")
    print("")





