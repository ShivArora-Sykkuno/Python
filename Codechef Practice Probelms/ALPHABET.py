string = input()
lst = []
test = int(input())
for i in range(test):
    lst.append(input())
for j in range(test):
    for i in lst[j]:
        if i in string:
            FLAG = 1
        else:
            FLAG = 0
            break
    if FLAG == 1:
        print("Yes")
    else:
        print("No")