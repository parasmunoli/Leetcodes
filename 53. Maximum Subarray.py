class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = 0
        num = 0
        max_num = float('-inf')

        while curr < len(nums):
            num += nums[curr]

            if num > max_num:
                max_num = num

            if num < 0:
                num = 0

            curr += 1

        return max_num