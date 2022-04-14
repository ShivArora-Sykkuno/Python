def removeElement(nums, val):
    while (val in nums):
        nums.remove(val)
    return len(nums)

for _ in range(int(input())):
    nums = list(map(int, input().split()))
    val = int(input())
    print(removeElement(nums, val))