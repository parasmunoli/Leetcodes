def maximizeSum(nums, k):
    score = 0
    while k != 0:
        score += max(nums)
        i = nums.index(max(nums))
        nums[i] += 1 
        k -= 1
    return score
nums = [1,2,3,4,5]
k = 3
print(maximizeSum(nums,k))