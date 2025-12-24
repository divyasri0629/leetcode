class Solution:
    def mySqrt(self, x: int) -> int:
        # Handle the base case for x = 0
        if x == 0:
            return 0
        
        left, right = 0, x
        
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        
        # After the loop ends, `right` will be the largest integer such that `right * right <= x`
        return right

# Example usage:
solution = Solution()

# Test cases
print(solution.mySqrt(4))  # Output: 2
print(solution.mySqrt(8))  # Output: 2
print(solution.mySqrt(16)) # Output: 4
print(solution.mySqrt(10)) # Output: 3
