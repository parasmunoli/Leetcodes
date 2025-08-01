class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def count_steps(n, curr, next_curr):
            steps = 0
            while curr <= n:
                steps += min(n + 1, next_curr) - curr
                curr *= 10
                next_curr *= 10
            return steps
        curr = 1
        k -= 1

        while k > 0:
            steps = count_steps(n, curr, curr + 1)
            if steps <= k:
                curr += 1
                k -= steps
            else:
                curr *= 10
                k -= 1

        return curr

