class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        b=[]
        for i in s:
            if i not in b:
                b.append(i)
                
                d[i]=1
            else:
                d[i]+=1
            r=""
            for j in sorted(d,key=d.get,reverse=True):
                r+=j*d[j]
        return r