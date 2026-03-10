class Solution:
    def minimumAverage(self, nums: List[int]) ->float:
        a=[]
        while(nums):
            mi=min(nums)
            mx=max(nums)
            avgg=(mi+mx)/2
            a.append(avgg)
            nums.remove(mi)
            nums.remove(mx)
        return min(a)