class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = set()
        n = len(digits)

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i != j and j != k and i != k:
                        d1, d2, d3 = digits[i], digits[j], digits[k]
                        if d1 == 0:
                            continue

                        if d3 % 2 != 0:
                            continue

                        number = d1 * 100 + d2 * 10 + d3
                        result.add(number)
        return sorted(result)
