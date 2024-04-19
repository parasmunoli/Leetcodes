def arithmeticTriplets(nums, diff):
    seen = set(nums)
    count = 0
    for num in nums:
        if num + diff in seen and num + 2 * diff in seen:
            count += 1 
    return count

nums = [0, 1, 4, 6, 7, 10]
diff = 3
print(arithmeticTriplets(nums, diff))