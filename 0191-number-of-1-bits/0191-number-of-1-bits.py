class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        a=bin(n)[2:]
        for i in a:
            if i=='1':
                count+=1
        return count