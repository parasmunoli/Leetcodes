class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"

        current = "1"

        for _ in range(2, n + 1):
            next_seq = ""
            i = 0
            while i < len(current):
                count = 1
                while i + 1 < len(current) and current[i] == current[i + 1]:
                    i += 1
                    count += 1
                next_seq += str(count) + current[i]
                i += 1
            current = next_seq
        return current
