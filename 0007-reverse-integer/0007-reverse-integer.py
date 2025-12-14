class Solution:
    def reverse(self, x: int) -> int:
        g=-1 if x<0 else 1
        x_abs=abs(x)
        revs=int(str(x_abs)[::-1])
        revs=revs*g
        if revs<-2**31 or revs>=2**31-1:
            return 0
        return revs
