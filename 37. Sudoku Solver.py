import pprint as pp


class Solution(object):
    def solveSudoku(self, board):
        self.traceBack(board)
        pp.pprint(board)
        return board

    def optimizedList(self, board, row, col):
        optimizedList = set('123456789')
        for i in range(9):
            optimizedList.discard(board[row][i])
            optimizedList.discard(board[i][col])

        rowSq = (row // 3) * 3
        colSq = (col // 3) * 3

        for r in range(rowSq, rowSq + 3):
            for c in range(colSq, colSq + 3):
                optimizedList.discard(board[r][c])
        return optimizedList

    def traceBack(self, board):
        empty_cells = []
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    valid_numbers = self.optimizedList(board, row, col)
                    empty_cells.append((row, col, len(valid_numbers), valid_numbers))

        if not empty_cells:
            return True

        empty_cells.sort(key=lambda x: x[2])
        row, col, _, valid_numbers = empty_cells[0]

        for num in valid_numbers:
            board[row][col] = num
            if self.traceBack(board):
                return True
            board[row][col] = '.'
        return False


solution = Solution()