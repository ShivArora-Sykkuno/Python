
N, K = map(int, input().split())
arr = list(map(int, input().split()))
res = 0
for i in arr:
    res = max(res, K - i)
print(res)