def differenceOfSum(nums):
    num_sum = 0
    digi_sum = 0
    for i in range(len(nums)):
        num_sum += nums[i]
        while nums[i] != 0:
            digit = nums[i]%10
            digi_sum += digit
            nums[i] = int(nums[i]/10)
    return abs(num_sum-digi_sum)
    
nums = [1,15,6,3]
print(differenceOfSum(nums))