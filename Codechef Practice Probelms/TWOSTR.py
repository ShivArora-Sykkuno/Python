for _ in range(int(input())):
    string = input()
    T = input()
    N = len(string)
    cnt = 0
    for i in range(N):
        if string[i] == T[i] or string[i] == "?" or T[i] == "?":
            cnt += 1
    if cnt == N:
        print("Yes")
    else:
        print("No")