for _ in range(int(input())):
    S = input()
    length = len(S) // 2
    if len(S) % 2 == 0:
        if sorted(S[:length]) == sorted(S[length:]):
            print("YES")
        else:
            print("NO")
    else:
        if sorted(S[:length]) == sorted(S[length + 1:]):
            print("YES")
        else:
            print("NO")
