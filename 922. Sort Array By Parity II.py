def sortArrayByParityII(nums):
    eve_index = 0
    odd_index = 1
    ans = [0]*len(nums)
    for i in range(len(nums)):
        if nums[i]%2 == 0:
            ans[eve_index] = nums[i]
            eve_index += 2
        else:
            ans[odd_index] = nums[i]
            odd_index += 2  
    return ans

nums = [4,2,5,7]
print(sortArrayByParityII(nums))