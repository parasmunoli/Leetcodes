def countKDifference(nums, k):
    count = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if abs(nums[i]-nums[j]) == k and i < j:
                count += 1
    return count
        
    
nums = [1,2,2,1]
k = 1
print(countKDifference(nums, k))