class Solution(object):
    
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        Valid = True

        for i in range(9):
            col = []
            for x in range(9):
                col.append(board[x][i])
            y = 8
            while y>=0:
                if col[y] == '.' or col[y] == '':
                    col.pop(y)
                y-=1
            col.sort()
            for j in range(len(col)-1):

                if col[j] == col[j+1]:
                    Valid = False

        for i in range(9):
            row = []
            for x in range(9):
                row.append(board[i][x])
            y = 8
            while y>=0:
                if row[y] == '.' or row[y] == '':
                    row.pop(y)
                y-=1
            row.sort()
            for j in range(len(row)-1):

                if row[j] == row[j+1]:
                    Valid = False

        for i in range(3):
            for j in range(3):
                sqr = []
                for r in range(3):
                    for c in range(3):
                        sqr.append(board[3*i+r][3*j+c])


                y=8
                while y>=0:
                    if sqr[y] == '.' or sqr[y] == '':
                        sqr.pop(y)
                    y-=1
                sqr.sort()

                for x in range(len(sqr)-1):

                    if sqr[x] == sqr[x+1]:
                        Valid = False
        return Valid
