class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = {}

        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        odd_freqs = []
        even_freqs = []

        for count in freq.values():
            if count % 2 == 0:
                even_freqs.append(count)
            else:
                odd_freqs.append(count)

        max_odd = odd_freqs[0]
        for val in odd_freqs:
            if val > max_odd:
                max_odd = val

        min_even = even_freqs[0]
        for val in even_freqs:
            if val < min_even:
                min_even = val

        return max_odd - min_even
