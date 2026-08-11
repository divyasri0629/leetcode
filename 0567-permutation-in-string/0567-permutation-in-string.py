class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        c=[0]*26
        d=[0]*26
        for i in range(len(s1)):
            c[ord(s1[i])-ord("a")]+=1
            d[ord(s2[i])-ord("a")]+=1
        if c==d:
            return True
        i=0
        for j in range(len(s1),len(s2)):
            d[ord(s2[j])-ord("a")]+=1
            d[ord(s2[i])-ord("a")]-=1
            i+=1
            if c==d:
            
                return True
        return False
