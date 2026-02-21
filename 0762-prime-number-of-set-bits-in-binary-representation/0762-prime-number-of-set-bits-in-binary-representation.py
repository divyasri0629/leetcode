class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count=0
        for i in range(left,right+1):
            n=bin(i)[2:]
            c=n.count("1")
            if c>1:
                prime=True
                for j in range(2,int(math.sqrt(c))+1):
                    if c%j==0:
                        prime=False
                        break
                if prime:
                    count+=1
        return count
            