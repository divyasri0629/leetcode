class Solution:
    def bitwiseComplement(self, n: int) -> int:
        a=""
        b=bin(n)[2:]
        for i in b:
            if i=="0":
                a+="1"
            else:
                a+="0"
        return int(a,2)