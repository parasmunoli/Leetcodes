class Solution(object):
    def minDifficulty(self, jobDifficulty, d):
        self.n = len(jobDifficulty)
        if self.n < d:
            return -1

        self.dp = [[-1] * (d + 1) for _ in range(self.n)]

        return self.helper(d, 0, jobDifficulty)

    def helper(self, d, i, jobDifficulty):
        if d == 0 and i == self.n:
            return 0
        if d == 0 or i == self.n:
            return float('inf')
        if self.dp[i][d] != -1:
            return self.dp[i][d]

        max_val = jobDifficulty[i]
        min_val = float('inf')

        for j in range(i, self.n):
            max_val = max(max_val, jobDifficulty[j])
            future = self.helper(d - 1, j + 1, jobDifficulty)

            if future != float('inf'):
                min_val = min(min_val, future + max_val)

        self.dp[i][d] = min_val
        return min_val
        