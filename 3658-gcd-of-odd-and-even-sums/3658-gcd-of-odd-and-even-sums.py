import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        a=[]
        b=[]
        for i in range(2*n):
            if i%2:
                a.append(i)
            else:
                b.append(i)
            o=sum(a)
            e=sum(b)
        return math.gcd(o,e)