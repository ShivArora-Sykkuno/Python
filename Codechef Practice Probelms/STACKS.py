for _ in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    Stack = [arr[0]]

    for i in range(1, N):

        point_1 = 0
        point_2 = len(Stack) - 1
        temp = 0
        while point_1 <= point_2:
            mid = (point_1 + point_2) // 2
            if Stack[mid] > arr[i]:
                res = mid
                point_2 = mid - 1
                temp = 1
            else:
                point_1 = mid + 1
        if temp == 1:
            Stack[res] = arr[i]
        else:
            Stack.append(arr[i])
    print(len(Stack), end=' ')
    for i in Stack:
        print(i, end=' ')
    print()
