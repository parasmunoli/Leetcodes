from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words or not words[0]:
            return []

        word_len = len(words[0])
        num_words = len(words)
        window_len = word_len * num_words
        word_count = Counter(words)
        n = len(s)

        result = []

        for i in range(word_len):
            left = i
            right = i
            curr_count = Counter()
            words_used = 0

            while right + word_len <= n:
                word = s[right:right + word_len]
                right += word_len

                if word in word_count:
                    curr_count[word] += 1
                    words_used += 1

                    while curr_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        curr_count[left_word] -= 1
                        words_used -= 1
                        left += word_len

                    if words_used == num_words:
                        result.append(left)

                else:
                    curr_count.clear()
                    words_used = 0
                    left = right

        return result