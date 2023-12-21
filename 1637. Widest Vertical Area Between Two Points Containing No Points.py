class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        s = set()
        res = 0
        for i in points:
            s.add(i[0])
        sorted_set = sorted(s)
        for i in range(1, len(sorted_set)):
            res = max(res, sorted_set[i] - sorted_set[i-1])
        return res