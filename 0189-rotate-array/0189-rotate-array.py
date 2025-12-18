class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        b = []

        # take last k elements
        for i in range(n - k, n):
            b.append(nums[i])

        # take first n-k elements
        for i in range(n - k):
            b.append(nums[i])

        # copy back into nums (in-place)
        for i in range(n):
            nums[i] = b[i]

