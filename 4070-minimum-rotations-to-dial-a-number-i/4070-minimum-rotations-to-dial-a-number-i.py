class Solution:
    def minRotations(self, s: str) -> int:
        a = []
        last = 0

        for i in range(len(s)):
            b = abs(last - int(s[i]))
            b = min(b, 10 - b)
            a.append(b)
            last = int(s[i])

        return sum(a)