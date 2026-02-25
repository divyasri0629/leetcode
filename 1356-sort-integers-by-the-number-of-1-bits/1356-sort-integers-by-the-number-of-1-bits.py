class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        # Sort using a lambda function as key
        # First sort by number of 1s in binary, then by number itself
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))