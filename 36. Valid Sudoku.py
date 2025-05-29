class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                if val in rows[i]:
                    return False
                if val in cols[j]:
                    return False
                if val in boxes[i // 3][j // 3]:
                    return False

                rows[i].add(val)
                cols[j].add(val)
                boxes[i // 3][j // 3].add(val)

        return True