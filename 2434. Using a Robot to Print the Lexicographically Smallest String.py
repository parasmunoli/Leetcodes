class Solution(object):
    def robotWithString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)

        min_suffix = [None] * n
        min_suffix[-1] = s[-1]
        for i in range(n - 2, -1, -1):
            min_suffix[i] = min(s[i], min_suffix[i + 1])

        t = []
        result = []
        i = 0

        while i < n or t:
            if i < n:
                t.append(s[i])
                i += 1

            while t and (i == n or t[-1] <= min_suffix[i]):
                result.append(t.pop())

        return ''.join(result)