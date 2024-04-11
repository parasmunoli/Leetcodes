def buildArray(nums):
        ans = [0] * len(nums)
        for i in range(len(nums)):
            ans[i] = nums[nums[i]]
        return ans
    
nums = [0,1,2,4,5,3]
print(buildArray(nums))