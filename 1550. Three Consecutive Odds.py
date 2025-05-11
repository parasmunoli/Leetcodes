class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = 0

        if not arr:
            return False

        for i in arr:
            if i % 2 == 0:
                count = 0
            else:
                count += 1
                if count == 3:
                    return True

        return False