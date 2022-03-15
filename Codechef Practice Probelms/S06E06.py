for test in range(int(input())):
    n, k = [int(x) for x in input().split()]
    digits = [int(x) for x in list(str(n))]
    digits.sort()
    arr = {}
    for i in range(10):
        arr[i] = 0
    for i in digits:
        arr[i] += 1
    while(k > 0):
        for i in arr:
            if(i < 9 and k > 0 and arr[i]):
                if(arr[i] >= k):
                    arr[i] -= k
                    arr[i+1] += k
                    k = 0
                else:
                    k = k - arr[i]
                    arr[i+1] += arr[i]
                    arr[i] = 0
        k -= 1
    ans = 1
    for i in arr:
        ans = ans*(i**arr[i])
    print(ans)
