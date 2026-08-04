class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett=set()
        j=0
        a=0
        for i in range(len(s)):
            while s[i] in sett:
                sett.remove(s[j])
                j+=1
            sett.add(s[i])
            a=max(a,i-j+1)


        return a