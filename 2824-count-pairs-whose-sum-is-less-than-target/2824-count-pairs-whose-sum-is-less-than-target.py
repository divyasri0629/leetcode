class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        l = 0
        c = 0
        
        for i in range(len(nums)):
            for r in range(l + 1, len(nums)):
                if nums[l] + nums[r] < target:
                    c += 1
            l += 1
            
        return c