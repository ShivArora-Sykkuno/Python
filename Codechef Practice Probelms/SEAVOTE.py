for i in range(int(input())):
    n = int(input())
    x = list(map(int, input().strip().split(' ')[:n]))
    if sum(x) < 100:
        print("NO")
    elif sum(x) == 100:
        print("YES")
    else:
        if sum(x) - 100 < len(x) - x.count(0):
            print("YES")
        else:
            print("NO")



