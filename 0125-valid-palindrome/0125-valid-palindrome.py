class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=""
        i=0
        while i<len(s):
            if s[i].isalnum():
                a+=s[i]
            i+=1
        if a.lower()==a.lower()[::-1]:
            return True
        else:
            return False
