class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reachable = 0

        for i, jump in enumerate(nums):
            if i > max_reachable:
                return False  # you're stuck
            max_reachable = max(max_reachable, i + jump)

        return True