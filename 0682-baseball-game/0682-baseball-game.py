class Solution:
    def calPoints(self, operations: List[str]) -> int:
        a=[]
        for i in range(len(operations)):
            if operations[i]=="+":
                a.append(a[-1]+a[-2])
            elif operations[i]=="D":
                a.append(2*a[-1])
            elif operations[i]=="C":
                a.pop()
            else:
                a.append(int(operations[i]))
        return sum(a)
