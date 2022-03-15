n, a, b = [int(x) for x in input().split()]
arrangement = input()
mins, maxs = min(a, b), max(a, b)
a, b = maxs, mins
last_seated = 0
counts = 0
for i in arrangement:
    if i == "." and last_seated == 0 and a > 0:
        last_seated = 1 - last_seated
        a -= 1
        counts += 1
    elif i == "." and last_seated == 1 and b > 0:
        last_seated = 1 - last_seated
        b -= 1
        counts += 1
    else:
        minn, maxx = min(a, b), max(a, b)
        a, b = maxx, minn
        last_seated = 0

print(counts)





