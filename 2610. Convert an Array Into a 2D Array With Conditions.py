class Solution(object):
    def findMatrix(self, nums):
        count_nums = {}
        ans = []
        for num in nums:
            if num not in count_nums:
                count_nums[num] = 0
            idx = count_nums[num]
            if idx == len(ans):
                ans.append([])
            ans[idx].append(num)
            count_nums[num] += 1
        return ans