def findMaxK(nums):
    max_k = -1
    num_set = set(nums)

    for num in nums:
        if -num in num_set and num > max_k:
            max_k = num

    return max_k if max_k != -1 else -1
nums = [-1,10,6,7,-7,1]
print(findMaxK(nums))