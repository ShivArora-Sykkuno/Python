def singleNumber(self, nums: List[int]) -> List[int]:
    res = 0
    for x in nums:
        res = res ^ x

    mask = res & (-res)
    res1 = 0
    res2 = 0
    for x in nums:
        if mask & x == 0:
            res1 = res1 ^ x
        else:
            res2 = res2 ^ x
    return [res1, res2]

