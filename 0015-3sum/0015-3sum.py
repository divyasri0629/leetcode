class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()  # Sort array first
        result = []
        n = len(nums)

        for i in range(n - 2):
            # Skip duplicates for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            # Two-pointer approach without while loop using a for-like simulation
            # Using left and right increments inside a single inner loop
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # Increment left pointer and skip duplicates
                    left_val = nums[left]
                    while left < right and nums[left] == left_val:
                        left += 1

                    # Decrement right pointer and skip duplicates
                    right_val = nums[right]
                    while left < right and nums[right] == right_val:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result