t = int(input())
for i in range(0, t):
    s = input()

    a = "dehllloorw"
    if "".join(sorted(s)) == a:
        print("Yes")
    else:
        print("No")