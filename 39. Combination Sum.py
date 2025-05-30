class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(start, target, path):
            if target == 0:
                result.append(path[:])
                return
            if target < 0:
                return
            for i in range(start, len(candidates)):
                # Choose current number and explore further
                backtrack(i, target - candidates[i], path + [candidates[i]])

        backtrack(0, target, [])
        return result