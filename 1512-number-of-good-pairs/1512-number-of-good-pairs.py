class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        a={}
        c=0
        for i in nums:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
            b=list(a.values())
        for i in b:
            c+=(i*(i-1))//2
        return c