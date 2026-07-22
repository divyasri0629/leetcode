class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d = {}

        for num in nums:
            s = 0
            temp = num

            while temp > 0:
                s += temp % 10
                temp //= 10

            if s not in d:
                d[s] = []

            d[s].append(num)

        ans = -1

        for values in d.values():
            if len(values) >= 2:
                values.sort(reverse=True)
                ans = max(ans, values[0] + values[1])

        return ans