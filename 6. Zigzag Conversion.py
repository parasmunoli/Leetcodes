class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        result = []
        n = len(s)
        cycle_len = 2 * numRows - 2

        for row in range(numRows):
            for j in range(0, n, cycle_len):
                if j + row < n:
                    result.append(s[j + row])

                if row != 0 and row != numRows - 1:
                    diagonal_idx = j + cycle_len - row
                    if diagonal_idx < n:
                        result.append(s[diagonal_idx])

        return ''.join(result)