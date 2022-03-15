class Solution:
    def jump(self, array):
        if len(array) == 1:
            return 0
        jumps, maxReach, steps = 0, array[0], array[0]
        for idx in range(1, len(array)-1):
            maxReach = max(maxReach, idx+array[idx])
            steps -= 1
            if steps == 0:
                jumps += 1
                steps = maxReach-idx
        return jumps+1