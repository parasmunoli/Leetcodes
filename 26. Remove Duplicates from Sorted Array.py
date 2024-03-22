def removeDuplicates(nums):
        count = 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                pass
            else:
                nums[count + 1] = nums[i + 1]
                count += 1
        return len(set(nums))

nums = [1,1,2]
print(removeDuplicates(nums))