

n = int(input())
cost = list(map(int, input().split()))

types = list(map(int, input().split()))
res_ARR = [1000000, 1000000, 1000000, 1000000]

for i in range(n):
    res_ARR[types[i]] = min(res_ARR[types[i]], cost[i])
if (res_ARR[1] + res_ARR[2]) < res_ARR[3]:
    print(res_ARR[1] + res_ARR[2])
else:
    print(res_ARR[3])
