class Solution:
    def sortSentence(self, s: str) -> str:
        di={}
        for word in s.split():
            w=int(word[-1])
            l=word[:-1]
            di[w]=l
        return " ".join(di[i] for i in range(1,len(di)+1))
