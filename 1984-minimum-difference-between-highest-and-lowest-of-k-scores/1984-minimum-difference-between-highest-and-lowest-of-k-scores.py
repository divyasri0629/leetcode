from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        
        nums.sort()
        m = float("inf")

        for i in range(len(nums)):
            for j in range(i + k - 1, len(nums)):
                diff = nums[j] - nums[i]
                m = min(m, diff)

        return m
