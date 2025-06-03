class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """

        def backtrack(row, cols, diag1, diag2):
            if row == n:
                count[0] += 1
                return

            for col in range(n):
                if col in cols or (row + col) in diag1 or (row - col) in diag2:
                    continue

                cols.add(col)
                diag1.add(row + col)
                diag2.add(row - col)

                backtrack(row + 1, cols, diag1, diag2)

                cols.remove(col)
                diag1.remove(row + col)
                diag2.remove(row - col)

        count = [0]
        backtrack(0, set(), set(), set())
        return count[0]