class Solution(object):
    def lengthAfterTransformations(self, s, t):
        """
        :type s: str
        :type t: int
        :rtype: int
        """
        alphCount = [0 for i in range(26)]
        aord = ord("a")
        for i in s:
            alphCount[ord(i) - aord] += 1
        for i in range(t):
            alphCount.insert(0, alphCount.pop(-1))
            alphCount[1] += alphCount[0]
        return sum(alphCount) % (10 ** 9 + 7)
