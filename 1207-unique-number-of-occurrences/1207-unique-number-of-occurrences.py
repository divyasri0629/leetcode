class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        a = {}

        for i in arr:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1

        values = list(a.values())

        for i in range(len(values)):
            for j in range(i + 1, len(values)):
                if values[i] == values[j]:
                    return False

        return True
        