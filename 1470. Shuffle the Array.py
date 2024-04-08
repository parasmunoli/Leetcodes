def shuffle(nums, n):
    li = []
    for i in range(n):
        li.append(nums[i])
        li.append(nums[n+i])
    return li

nums = [2,5,1,3,4,7]
n = 3
print(shuffle(nums,n))