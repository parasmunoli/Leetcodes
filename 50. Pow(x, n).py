class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def fast_pow(base, exp):
            if exp == 0:
                return 1.0
            half = fast_pow(base, exp // 2)
            if exp % 2 == 0:
                return half * half
            else:
                return half * half * base

        if n < 0:
            return 1 / fast_pow(x, -n)
        else:
            return fast_pow(x, n)