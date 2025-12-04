class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Find the shortest string length
        min_len = min(len(s) for s in strs)

        prefix = ""

        # Check each index
        for i in range(min_len):
            ch = strs[0][i]       # character from first string

            # Compare with all other strings
            for j in range(1, len(strs)):
                if strs[j][i] != ch:
                    return prefix   # mismatch → return result immediately

            # If all matched, add character
            prefix += ch

        return prefix
