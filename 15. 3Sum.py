class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        def twoSum(nums, i, target):
            low, high = i+1, len(nums)-1
            while low < high:
                addup = nums[low] + nums[high]
                if addup < target:
                    low += 1
                elif addup > target:
                    high -= 1
                else:
                    result.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1
                    while low < high and nums[low-1] == nums[low]:
                        low += 1

        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                target = -nums[i]
                twoSum(nums, i, target)

        return result