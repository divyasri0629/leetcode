class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a = []
        n = min(len(word1), len(word2))

        for i in range(n):
            a.append(word1[i])
            a.append(word2[i])

        # append remaining characters
        a.append(word1[n:])
        a.append(word2[n:])

        return ''.join(a)