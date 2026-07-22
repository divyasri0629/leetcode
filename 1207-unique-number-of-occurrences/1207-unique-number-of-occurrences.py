class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        a = {}

        for i in arr:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1

        values = list(a.values())

        value=set(values)
        if len(value)!=len(values):
            return False

        return True
        