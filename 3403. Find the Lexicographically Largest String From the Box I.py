from itertools import combinations


class Solution(object):
    def answerString(self, word, numFriends):
        """
        :type word: str
        :type numFriends: int
        :rtype: str
        """
        n = len(word)
        box = []

        for cuts in combinations(range(1, n), numFriends - 1):
            parts = []
            prev = 0
            for cut in cuts:
                parts.append(word[prev:cut])
                prev = cut
            parts.append(word[prev:])
            box.extend(parts)

        return max(box)