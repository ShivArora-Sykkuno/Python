def twoSum(nums, target):
    res = list()
    for i in range(len(nums)-1):
        if nums[i] + nums[i+1] == target:
            res.append(i)
            res.append(i+1)
            break
    return res


for _ in range(int(input())):
    nums = list(map(int, input().split()))
    target = int(input())
    print(twoSum(nums, target))