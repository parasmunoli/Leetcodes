from collections import defaultdict


class Solution(object):
    def clearStars(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = []
        char_indices = defaultdict(list)

        for idx, ch in enumerate(s):
            if ch != '*':
                stack.append(ch)
                char_indices[ch].append(len(stack) - 1)
            else:
                for c in range(26):
                    letter = chr(ord('a') + c)
                    if char_indices[letter]:
                        pos = char_indices[letter].pop()
                        stack[pos] = None
                        break

        return ''.join(ch for ch in stack if ch is not None)