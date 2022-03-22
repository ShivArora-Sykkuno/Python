from collections import deque

for _ in range(int(input())):
    N, K = map(int, input().split())
    string = input()
    temp = K + 1
    res = 0
    empty_str = ""
    for i in string:
        if i == ':':
            empty_str += ':'
        empty_str += i
    queue1 = deque()
    queue2 = deque()
    for i in range(len(empty_str)):
        if empty_str[i] == 'X':
            while queue1:
                queue1.pop()
            while queue2:
                queue2.pop()
        elif empty_str[i] == 'I':
            flag = False
            while queue1:
                if (temp - abs(queue1[0] - i)) > 0:
                    res += 1
                    flag = True
                    queue1.popleft()
                    break
                else:
                    queue1.popleft()
            if not flag:
                queue2.append(i)
        elif empty_str[i] == 'M':
            flagI = False
            while queue2:
                if (temp - abs(queue2[0] - i)) > 0:
                    res += 1
                    flagI = True
                    queue2.popleft()
                    break
                else:
                    queue2.popleft()
            if not flagI:
                queue1.append(i)
    print(res)
