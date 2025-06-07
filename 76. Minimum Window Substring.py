from collections import Counter


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""

        dict_t = Counter(t)
        required = len(dict_t)
        left, right = 0, 0
        formed = 0
        window_counts = {}

        min_len = float('inf')
        min_left = 0

        while right < len(s):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1

            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1

            while left <= right and formed == required:
                char = s[left]

                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_left = left

                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1

                left += 1

            right += 1

        return "" if min_len == float('inf') else s[min_left:min_left + min_len]