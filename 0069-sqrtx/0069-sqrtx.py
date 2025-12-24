class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return x
        i=0
        j=x
        while i<=j:
            mid=(i+j)//2
            if mid*mid==x:
                return mid
            elif mid*mid<x:
                i=mid+1
            else:
                j=mid-1

        return j
        
