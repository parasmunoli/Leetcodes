class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            revString = str(x)[::-1]
            x = int(revString)

        else:
            revString = '-' + str(-1 * x)[::-1]
            x = int(revString)

        if -(2 ** 31) >= x or x >= 2 ** 31 - 1:
            return 0
        return x