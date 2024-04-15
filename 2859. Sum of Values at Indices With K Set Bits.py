def sumIndicesWithKSetBits(nums, k):
    sum = 0
    for i, x in enumerate(nums):
        if bin(i).count('1') == k:
            sum = sum + x
    return sum
    
nums = [5,10,1,5,2]
k = 1
print(sumIndicesWithKSetBits(nums,k))