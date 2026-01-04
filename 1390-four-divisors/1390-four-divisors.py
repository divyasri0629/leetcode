from typing import List
import math

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0

        for i in nums:
            di = []  # reset for each number

            for j in range(1, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    di.append(j)
                    if j != i // j:
                        di.append(i // j)

                if len(di) > 4:   # early stop → avoids TLE
                    break

            if len(di) == 4:
                total += sum(di)

        return total
