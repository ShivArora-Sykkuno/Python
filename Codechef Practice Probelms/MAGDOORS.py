for _ in range(int(input())):
    string = input()
    res = 0
    if '0' not in string:
        print(0)
        continue
    if string[0] == '0':
        res += 1

    for i in range(len(string)):
        if string[i: i + 2] == '01' or string[i: i + 2] == '10':
            res += 1
    print(res)
