class Solution(object):
    def minDeletion(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        distinct = len(freq)

        if distinct <= k:
            return 0

        freq_list = []
        for count in freq.values():
            freq_list.append(count)
        freq_list.sort()

        remove_count = distinct - k
        deletions = 0
        for i in range(remove_count):
            deletions += freq_list[i]

        return deletions