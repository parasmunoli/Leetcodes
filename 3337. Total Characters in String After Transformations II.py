class Solution(object):
    def lengthAfterTransformations(self, s, t, nums):
        """
        :type s: str
        :type t: int
        :type nums: List[int]
        :rtype: int
        """
        if t == 0:
            return len(s) % (10 ** 9 + 7)

        MOD = 10 ** 9 + 7
        n = 26

        def mat_mul(a, b):
            result = [[0] * n for _ in range(n)]
            for i in range(n):
                for k in range(n):
                    if a[i][k]:
                        for j in range(n):
                            if b[k][j]:
                                result[i][j] = (result[i][j] + (a[i][k] * b[k][j])) % MOD
            return result

        def mat_pow(mat, power):
            if power == 0:
                return [[1 if i == j else 0 for j in range(n)] for i in range(n)]
            if power == 1:
                return mat

            half = mat_pow(mat, power // 2)
            if power % 2 == 0:
                return mat_mul(half, half)
            return mat_mul(mat_mul(half, half), mat)

        trans_mat = [[0] * n for _ in range(n)]
        for i in range(n):
            num = nums[i]
            if num:
                for j in range(num):
                    next_char = (i + j + 1) % n
                    trans_mat[i][next_char] = 1

        char_count = [0] * n
        for c in s:
            char_count[ord(c) - ord('a')] += 1

        final_mat = mat_pow(trans_mat, t)

        result = 0
        for i in range(n):
            if char_count[i]:
                for j in range(n):
                    if final_mat[i][j]:
                        result = (result + (char_count[i] * final_mat[i][j])) % MOD

        return result