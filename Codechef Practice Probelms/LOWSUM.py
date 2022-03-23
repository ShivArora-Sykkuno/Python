for _ in range(int(input())):
    K, Q = map(int, input().split())
    arr_1 = list(map(int, input().split()))
    arr_2 = list(map(int, input().split()))
    arr_1.sort()
    arr_2.sort()
    temp_arr = []
    for i in range(Q):
        temp_arr.append(int(input()))
    res_arr = []
    for i in range(min(K, 10001)):
        for j in range(min(K, 10001 // (i + 1))):
            res_arr.append(arr_1[i] + arr_2[j])

    res_arr.sort()
    for i in temp_arr:
        print(res_arr[i - 1])