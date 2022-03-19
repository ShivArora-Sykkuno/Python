for _ in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    temp = 0
    if arr[0] == 1 and arr[N // 2] == 7:
        for i in range(N // 2):
            if arr[i] == arr[-i - 1] and arr[i + 1] - arr[i] <= 1 and arr[i] <= 7:
                temp += 1
            else:
                break
        if temp == N // 2:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
