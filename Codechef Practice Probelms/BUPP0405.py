for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    even = 0
    for i in arr:
        if bin(i).count('1') % 2 == 0:
            even += 1
    odd = n - even
    for __ in range(m):
        x = int(input())
        print(f"{str(even)} {str(odd)}" if bin(x).count('1') % 2 == 0 else f"{str(odd)} {str(even)}")