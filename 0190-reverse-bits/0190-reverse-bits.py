class Solution:
    def reverseBits(self, n: int) -> int:
        a=bin(n)[2:]
        a=a.zfill(32)
        b=(a)[::-1]
        return int(b,2)
        