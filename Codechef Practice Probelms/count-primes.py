def countPrimes(n):
    if n == 0 or n == 1 or n == 2: return 0
    PrimeTable = [True] * (n)
    p = 2
    while p ** 2 < n:
        if PrimeTable[p] == True:
            for i in range(p ** 2, n, p): PrimeTable[i] = False
        p += 1
    return sum(PrimeTable[2:])