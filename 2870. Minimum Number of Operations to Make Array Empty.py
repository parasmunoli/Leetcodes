class Solution(object):
    def minOperations(self, nums):
        counts = {}
        result = 0
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        for count in counts.values():
            if count == 1:
                return -1
            if count % 3 == 1:
                result += (count // 3) - 1
                result += 2
            else:
                result += count // 3
                result += (count % 3) // 2
        return result        