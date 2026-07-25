class Solution:
    def maxProduct(self, n: int) -> int:
        a=1
        b=[]
        c=0
        d=1
        while n>0:
            b.append(n%10)
            n//=10
        c=b.sort()
        if len(b)>1:
            for i in range(len(b)):
                d= b[-1]*b[-2]
        return d