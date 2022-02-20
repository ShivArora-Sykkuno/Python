
n, q = map(int, input().split())
arr = list(map(int, input().split()))
bit = [[0 for i in range(n+1)] for j in range(32)]
for i in range(n):
    for j in range(31):
        bit[j + 1][i + 1] = bit[j + 1][i]
        if arr[i] & (1 << j):
            bit[j + 1][i + 1] += 1

for _ in range(q):
    l, r = map(int, input().split())
    res = 0
    for i in range(1, 32):
        if ((r - l + 1) % 2) and (bit[i][r] - bit[i][l - 1] <= (r - l + 1) // 2):
            res += 1 << (i-1)
        elif bit[i][r] - bit[i][l - 1] < (r - l + 1) // 2:
            res += 1 << (i - 1)
    print(res)