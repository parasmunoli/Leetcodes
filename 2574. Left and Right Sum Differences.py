def leftRightDifference(nums):
    total_sum = sum(nums)
    left_sum = 0  
    answer = []

    for num in nums:
        right_sum = total_sum - left_sum - num
        answer.append(abs(left_sum - right_sum))
        left_sum += num

    return answer

nums = [10,4,8,3]
print(leftRightDifference(nums))