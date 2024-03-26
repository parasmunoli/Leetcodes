def missingNumber(nums):
    res = len(nums)

    for i in range(len(nums)):
        res += i - nums[i]
    
    return res
    
nums = [3,0,1]
print(missingNumber(nums))