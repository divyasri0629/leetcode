class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
       
        count = {}
        i = 0
        maximum = 0
        answer = 0

        for j in range(len(s)):
            count[s[j]] = count.get(s[j], 0) + 1

            maximum = max(maximum, count[s[j]])

            size = j - i + 1

            if size - maximum > k:
                count[s[i]] -= 1
                i += 1

            answer = max(answer, j - i + 1)

        return answer

