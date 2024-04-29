def findIntersectionValues(nums1, nums2):
    res = [0,0]
    for i in range(len(nums1)):
        if nums1[i] in nums2:
            res[0] += 1
    for j in range(len(nums2)):
        if nums2[j] in nums1:
            res[1] += 1
    return res

nums1 = [4,3,2,3,1]
nums2 = [2,2,5,2,3,6]
print(findIntersectionValues(nums1,nums2))