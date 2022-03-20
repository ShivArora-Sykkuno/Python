for _ in range(int(input())):
    N = int(input())
    arr = list(map(str, input()))
    temp = 0
    for i in arr:
        if i == '1':
            temp += 1
    print((temp * (temp + 1)) // 2)