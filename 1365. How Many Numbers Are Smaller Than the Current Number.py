def smallerNumbersThanCurrent(nums):
    numbers = {}
    sorted_nums = sorted(nums)
    for i in range(0, len(sorted_nums)):
        if sorted_nums[i] not in numbers:
            numbers[sorted_nums[i]] = i
            
    return [numbers[num] for num in nums]
nums = [8,1,2,2,3]
print(smallerNumbersThanCurrent(nums))