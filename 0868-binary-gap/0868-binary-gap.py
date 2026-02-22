class Solution:
    def binaryGap(self, n: int) -> int:
        a=bin(n)[2:]
        b=0
        for i in range(len(a)):
            if a[i]=='1': 
                for j in range(i+1,len(a)):
                    if a[j]=='1':
                        mi=j-i
                        b=max(mi,b)
                        break
        return b


        