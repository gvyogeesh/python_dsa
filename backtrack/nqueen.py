https://leetcode.com/problems/n-queens/

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.result = []
        self.cur = [['.'] * n for i in range(n)]
        # print self.cur
        
        def issafe(row, col):
            for i in range(n):
                for j in range(n):
                    if self.cur[i][j] == 'Q':
                        #Same row
                        if i == row:
                            return False
                        #Same col
                        if j == col:
                            return False
                        #Diagonal
                        if (i + j == row + col) or (i - j == row - col):
                            return False
            return True
                        
        
        def nqueenutil(n, row):
            if row == n:
                # print self.cur
                res = []
                for i in self.cur:
                    res.append("".join(i))
                self.result.append(res)
                return
            for i in range(n):
                if issafe(row, i) == True:
                    self.cur[row][i] = 'Q'
                    nqueenutil(n, row+1)
                    self.cur[row][i] = '.'
        
        nqueenutil(n, 0)
        print self.result
        return self.result