class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)

        def get_board_value(label):
            quot, rem = divmod(label - 1, n)
            row = n - 1 - quot
            col = rem if (quot % 2 == 0) else n - 1 - rem
            return board[row][col]

        visited = set()
        queue = deque([(1, 0)])

        while queue:
            square, moves = queue.popleft()
            for i in range(1, 7):
                next_square = square + i
                if next_square > n * n:
                    continue
                val = get_board_value(next_square)
                dest = val if val != -1 else next_square
                if dest == n * n:
                    return moves + 1
                if dest not in visited:
                    visited.add(dest)
                    queue.append((dest, moves + 1))

        return -1