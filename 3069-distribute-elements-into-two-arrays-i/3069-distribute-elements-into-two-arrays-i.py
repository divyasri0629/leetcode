class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        a=[]
        b=[]
        a.append(nums[0])
        b.append(nums[1])
        if len(nums)>2:
            for i in range(2,len(nums)):
                if a[-1]>b[-1]:
                    a.append(nums[i])
                else:
                    b.append(nums[i])
        return a+b 