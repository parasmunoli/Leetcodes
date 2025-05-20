class Solution(object):
    def isZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: bool
        """
        n = len(nums)
        delta = [0] * (n + 1)

        for l, r in queries:
            delta[l] += 1
            if r + 1 < n:
                delta[r + 1] -= 1

        count = [0] * n
        curr = 0
        for i in range(n):
            curr += delta[i]
            count[i] = curr

        for i in range(n):
            if nums[i] > count[i]:
                return False
        return True