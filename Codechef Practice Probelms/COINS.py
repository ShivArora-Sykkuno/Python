D = {0: 0}


def solve(n):
    if n in D:
        return D[n]
    else:
        D[n] = max(n, solve(n // 2) + solve(n // 3) + solve(n // 4))
        return D[n]


while True:
    N = int(input())
    print(solve(N))
