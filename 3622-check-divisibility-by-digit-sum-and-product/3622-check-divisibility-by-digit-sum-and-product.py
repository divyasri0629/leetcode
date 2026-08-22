class Solution:
    def checkDivisibility(self, n: int) -> bool:
        c=n
        a=0
        b=1
        while n>0:
            d=n%10 
            a+=d
            b*=d
            n//=10
        if c%(a+b)==0:
            return True
        else:
            return False      