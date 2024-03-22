def removeElement(nums, val):
        count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                pass
            else:
                nums[count] = nums[i]
                count += 1
        nums = nums[:count]
        return len(nums)
    
nums = [3,2,2,3]
val = 3
print(removeElement(nums,val))