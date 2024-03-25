def majorityElement(nums):
    dic = {}
    for i in nums:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    for key,value in dic.items():
        if value > len(nums)/2:
            num = key
            return num
        
nums = [3,2,3]
print(majorityElement(nums))