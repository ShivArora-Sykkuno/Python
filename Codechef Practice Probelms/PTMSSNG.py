
for _ in range(int(input())):
    N=int(input())
    x, y = 0, 0
    for i in range((4 * N)-1):
        I,J = map(int, input().split())
        x ^= I
        y ^= J
    print(x, y)
