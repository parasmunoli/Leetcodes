class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for current in intervals[1:]:
            last = merged[-1]

            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])  # Merge
            else:
                merged.append(current)

        return merged