def searchInsert(nums, target):
    if target in nums:
        return nums.index(target)
    else:
        count = 0
        for i in nums:
            if i < target:
                count += 1
            else:
                break
        return count
        
            
    
nums = [1,3,5,6]
target = 5
target1 = 2
target2 = 7
print(searchInsert(nums, target))
print(searchInsert(nums, target1))
print(searchInsert(nums, target2))