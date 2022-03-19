import math

for _ in range(int(input())):
    num = int(input())
    s = num * (num + 1) // 2
    if s % 2 == 0:
        temp = int((math.sqrt(4 + 8 * (num * num + num)) - 2) // 4)
        res = num - temp
        if temp * (temp + 1) // 2 == s // 2:
            res += (temp * (temp - 1) // 2) + ((num - temp) * ((num - temp) - 1) // 2)
        print(res)
    else:
        print(0)