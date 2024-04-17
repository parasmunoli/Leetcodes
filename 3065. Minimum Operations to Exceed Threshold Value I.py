def minOperations(nums, k):
    count = 0
    for i in range(len(nums)):
        if nums[i] < k:
            count += 1
    return count
    
nums = [2,11,10,1,3]
k = 10
print(minOperations(nums,k))