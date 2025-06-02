class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_map = {}

        for word in strs:
            key = ''.join(sorted(word))

            if key in anagram_map:
                anagram_map[key].append(word)
            else:
                anagram_map[key] = [word]

        return list(anagram_map.values())