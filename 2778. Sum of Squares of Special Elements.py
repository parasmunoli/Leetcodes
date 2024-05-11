def sumOfSquares(nums):
    sum = 0
    length = len(nums)
    for i in range(1,len(nums)+1):
        if length % i == 0:
            sum += nums[i-1]**2
    return sum
nums = [2,7,1,19,18,3]
print(sumOfSquares(nums))