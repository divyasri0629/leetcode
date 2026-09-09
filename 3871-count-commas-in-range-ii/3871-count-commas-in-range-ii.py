class Solution:
    def countCommas(self, n: int) -> int:
        a = 0
        x = 1000

        while x <= n:
            a += n - x + 1
            x *= 1000

        return a