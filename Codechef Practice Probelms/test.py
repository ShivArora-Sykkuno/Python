for _ in range(int(input())):
    num = int(input())
    res = 0
    list = []
    for i in range(1, num + 1):
        list.append(i)
    for i in range(num):
        if list[i] % 2 == 0:
            res += 1
    print(num - res)