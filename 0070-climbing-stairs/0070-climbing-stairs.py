class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        # Initialize the first two values for dp
        first, second = 1, 2
        
        # Compute the result iteratively
        for i in range(3, n + 1):
            first, second = second, first + second
        
        return second

# Example usage:
solution = Solution()

# Test cases
print(solution.climbStairs(2))  # Output: 2
print(solution.climbStairs(3))  # Output: 3
print(solution.climbStairs(4))  # Output: 5
print(solution.climbStairs(5))  # Output: 8
