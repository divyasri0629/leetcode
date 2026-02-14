class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a=0
        for i in range(len(prices)):
    
            for j in range(i+1,len(prices)):
            
                q=prices[j]-prices[i]
                a=max(a,q)
        return a