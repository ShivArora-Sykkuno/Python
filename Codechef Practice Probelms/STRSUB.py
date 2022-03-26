def solve(St, ele):
    S, E = St, ele
    res = E
    while St <= ele:
        m = (St + ele) // 2
        if m == 0:
            tarr_0 = arr_0[E]
            tarr_1 = arr_1[E]
        else:
            tarr_0 = arr_0[E] - arr_0[m - 1]
            tarr_1 = arr_1[E] - arr_1[m - 1]

        if tarr_0 <= K and tarr_1 <= K:
            res = m
            ele = m - 1
        else:
            St = m + 1
    return res


def solved(l, r):
    L, R = l, r
    res = L
    while l <= r:
        M = (l + r) // 2
        if r_e[M] <= L:
            l = M + 1
            res = M
        else:
            r = M - 1
    return res


for _ in range(int(input())):
    N, K, Q = map(int, input().split())
    String = input()
    arr_0 = [0] * (N)
    arr_1 = [0] * (N)
    for i in range(N):
        if i == 0:
            arr_0[0] = int('0' == String[i])
            arr_1[0] = int('1' == String[i])
        else:
            arr_0[i] = arr_0[i - 1] + int('0' == String[i])
            arr_1[i] = arr_1[i - 1] + int('1' == String[i])

    res = [0] * (N)
    r_e = [0] * (N)
    for i in range(N):
        temp = solve(0, i)
        r_e[i] = temp
        res[i] = i - temp + 1

    reans = [res[0]]
    for i in range(1, N):
        temp = res[i] + reans[i - 1]
        reans.append(temp)

    for _ in range(Q):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        ind = solved(l, r)
        fa = reans[r] - reans[ind]
        val = ind - l + 1
        fa += val * (val + 1) // 2
        print(fa)
