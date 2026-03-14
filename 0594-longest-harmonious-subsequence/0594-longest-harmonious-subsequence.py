class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq=Counter(nums)
        longest=0
        for i in freq:
            if i+1 in freq:
                longest=max(longest,freq[i]+freq[i+1])
        return longest