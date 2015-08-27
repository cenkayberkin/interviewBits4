
class Solution(object):
    solutions = []

    def isSafe(self,row,col,board):
    #     check row on left
        col1 = col
        while col1 > 0:
            col1 -= 1
            if board[row][col1] == "Q":
                return False
    #check upper diagonal
        col2 = col
        row2 = row
        while col2 > 0 and row2 > 0:
            col2 -= 1
            row2 -= 1
            if board[row2][col2] == "Q":
                return False

    # check lower diagonal
        col3 = col
        row3 = row
        while col3 > 0 and row3 < len(board) -1:
            col3 -= 1
            row3 += 1
            if board[row3][col3] == "Q":
                return False

        return True

    def solve2(self,board,col):
        if col >= len(board):
            tmp = []
            [tmp.append("".join(i)) for i in board]
            self.solutions.append(tmp)

        for i in range(len(board)):
            if self.isSafe(i,col,board):
                board[i][col] = "Q"
                self.solve2(board,col + 1)
                board[i][col] = "."

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = []
        for i in range(n):
            tmp = []
            for j in range(n):
                tmp.append('.')
            board.append(tmp)
        self.solutions = []
        self.solve2(board,0)
        return self.solutions


s = Solution()
print s.solveNQueens(4)