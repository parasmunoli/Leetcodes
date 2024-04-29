def sumCounts(nums):
    sum = 0
    for i in range(len(nums)):
        sub_arrays = set()
        for j in range(i,len(nums)):
            sub_arrays.add(nums[j])
            sum += len(sub_arrays)**2
    return sum             
                
nums = [1,1]
print(sumCounts(nums))