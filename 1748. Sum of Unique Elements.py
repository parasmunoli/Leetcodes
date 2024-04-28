def sumOfUnique(nums):
    res = []
    for i in nums:
        if nums.count(i) > 1:
            continue
        else:
            res.append(i)
    return sum(res)
    
nums = [1,2,3,2]
print(sumOfUnique(nums))