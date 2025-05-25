class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if not words:
            return 0

        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        length = 0
        used_center = False

        for word in list(word_count.keys()):
            rev = word[::-1]
            if word != rev and rev in word_count:
                pairs = min(word_count[word], word_count[rev])
                length += pairs * 4
                word_count[word] -= pairs
                word_count[rev] -= pairs

        for word in word_count:
            if word[0] == word[1]:
                pairs = word_count[word] // 2
                length += pairs * 4
                word_count[word] -= pairs * 2

        for word in word_count:
            if word[0] == word[1] and word_count[word] > 0:
                length += 2
                break

        return length