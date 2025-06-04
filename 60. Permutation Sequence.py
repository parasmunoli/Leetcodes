class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        from math import factorial

        digits = [str(i) for i in range(1, n + 1)]
        k -= 1
        result = ""

        for i in range(n - 1, -1, -1):
            f = factorial(i)
            index = k // f
            result += digits.pop(index)
            k %= f

        return result