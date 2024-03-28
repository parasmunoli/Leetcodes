def containsNearbyDuplicate(nums, k):
    num_indices = {}
    for i, num in enumerate(nums):
        if num in num_indices and i - num_indices[num] <= k:
            return True
        num_indices[num] = i
    return False
nums = [1,2,3,1]
k = 3
print(containsNearbyDuplicate(nums,k))