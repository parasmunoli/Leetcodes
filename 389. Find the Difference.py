class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        result = 0
        for ch in s:
            result ^= ord(ch)
        for ch in t:
            result ^= ord(ch)
        return chr(result)