for _ in range(int(input())):
    k = []
    for i in range(int(input())):
        k.append(list(map(int, input().split())))
    k.sort(key=lambda x: x[0], reverse=True)
    bomb = 1
    minn = k[0][0]
    for j in range(1, len(k)):
        if minn > k[j][1]:
            bomb += 1
            minn = k[j][0]
    print(bomb)
