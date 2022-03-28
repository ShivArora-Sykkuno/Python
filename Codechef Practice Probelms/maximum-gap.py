def maximumGap(nums):
    if len(nums) < 2:
        return 0
    else:
        max = 0
        nums.sort()
        for iterate in range(len(nums) - 1):
            if nums[iterate + 1] - nums[iterate] > max:
                max = nums[iterate + 1] - nums[iterate]
        return max