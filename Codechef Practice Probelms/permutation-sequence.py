def getPermutation(n, k):
    facts = [1]
    for i in range(1, n):
        facts.append(facts[-1] * i)
    nums = [str(i) for i in range(1, n + 1)]
    perm = ''
    m = n-1
    for i in range(n):
        leading = nums[k // facts[m]] if k % facts[m] != 0 else nums[k // facts[m] - 1]
        nums.remove(leading)
        perm += leading
        k = k % facts[m]
        m -= 1
    return perm

