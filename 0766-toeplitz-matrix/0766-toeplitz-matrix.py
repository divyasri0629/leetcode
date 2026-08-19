class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
    
        i=0

        while i<len(matrix)-1:
            j=0
            while j<len(matrix[0])-1:
                if matrix[i][j]!=matrix[i+1][j+1]:
            
                    return False
                j+=1
            i+=1
        return True
            
                
            

   