for _ in range(int(input())):
    arr = list(map(int, input().split()))
    res_arr = []
    if arr[0] == 1:
        res_arr.append(arr[1])
    else:
        if len(res_arr) >= 1:
            print(res_arr[len(res_arr) - 1])
            res_arr.pop()
        else:
            print("kuchbhi?")
