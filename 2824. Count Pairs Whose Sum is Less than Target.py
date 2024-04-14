def countPairs(nums, target):
    res = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] < target and i < j:
                res += 1            
    return res

nums = [-1,1,2,3,1]
target = 2
print(countPairs(nums,target))