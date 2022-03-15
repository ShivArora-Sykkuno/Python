for i in range(int(input())):
    z, y, a, b, c=map(int, input().split())
    if (z-y-a-b-c) >= 0:
        print("yes")
    else:
        print("no")
