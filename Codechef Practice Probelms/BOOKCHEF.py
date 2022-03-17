N, M = map(int, input().split())
friends = [int(x) for x in input().split()]
coll = []
for _ in range(M):
    f, p, book = input().split()
    coll.append([f, p, book])
res = []
n_res = []

for mem in coll:
    if int(mem[0]) in friends:
        res.append([int(mem[1]), mem[2]])
    else:
        n_res.append([int(mem[1]), mem[2]])


def get(item):
    return item[0]


res.sort(key=get, reverse=True)
n_res.sort(key=get, reverse=True)

for i in res:
    print(i[1])
for i in n_res:
    print(i[1])
