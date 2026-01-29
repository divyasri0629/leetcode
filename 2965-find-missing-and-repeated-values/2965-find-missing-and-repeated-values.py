class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        a=[]
        b=len(grid)
        c=[]
        for k in range(1,b*b+1):
            c.append(k)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] not in a:
                    a.append(grid[i][j])
                else:
                    d=grid[i][j]
        for k in (c):
            if k not in a:
                e=k
        return [d,e]