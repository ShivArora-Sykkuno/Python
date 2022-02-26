import bisect

for _ in range(int(input())):
    n = int(input())
    ARR = list(map(int, input().strip().split()))[:n]
    res = list()
    for i in range(0, len(ARR)):
        if len(res) > bisect.bisect(res, ARR[i]):
            res[bisect.bisect(res, ARR[i])] = ARR[i]
        else:
            res.append(ARR[i])
    print(len(res), end=" ")
    for i in res:
        print(i, end=" ")
    print()
