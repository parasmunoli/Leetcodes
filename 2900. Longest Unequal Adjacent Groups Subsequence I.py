class Solution(object):
    def getLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        altArrayofGroup = []
        for i in range(len(groups)):
            if i == 0:
                altArrayofGroup.append(i)
            elif groups[i] != groups[i - 1]:
                altArrayofGroup.append(i)

        output = []
        for j in altArrayofGroup:
            output.append(words[j])

        return output