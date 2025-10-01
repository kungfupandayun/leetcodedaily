#Given an m x n grid of characters board and a string word, return true if word exists in the grid.

#The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board) 
        m = len(board[0]) 

        def check(i,j,k):
            if k == len(word):
                return True

            if i>=len(board) or i<0 or j>=len(board[0]) or j<0 or board[i][j]!=word[k]:
                return False

            temp = board[i][j]
            board[i][j] = ''
                
            if check(i-1,j,k+1) or check(i+1,j,k+1) or check(i,j-1,k+1) or check(i,j+1,k+1):
                return True

            board[i][j] = temp
            return False
            

        for i in range(n):
            for j in range(m):
                if check(i,j,0):
                    return True

        return False