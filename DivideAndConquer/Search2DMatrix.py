#|      |
#|  MIN |
#|______|______
#       |P      |
#       |  MAX  | 
#       |       | 

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        def search(left,up,right,down):
            if left>right or up>down:
                return False
            
            if target<matrix[up][left] or target>matrix[down][right]:
                return False
            
            mid = (left+right)//2
            row = up
            while row<=down and matrix[row][mid]<=target:
                if matrix[row][mid] == target:
                    return True
                row+=1
                
            return search(left,row,mid-1,down) or search(mid+1,up,right,row-1)
        return search(0,0,len(matrix[0])-1,len(matrix)-1)