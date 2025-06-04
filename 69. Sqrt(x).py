class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x

        iterX = x / 2
        for i in range(1000):
            iterX = 0.5 * (iterX + x / iterX)

        return int(iterX)