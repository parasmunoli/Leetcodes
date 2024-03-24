def merge(nums1, m, nums2, n):
    nums3 = []
    for i in range(m):
        nums3.append(nums1[i])
    for i in range(n):
        nums3.append(nums2[i])
    for i, num in enumerate(sorted(nums3)):
        nums1[i] = num

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
n,m = 3,3
print(merge(nums1, m, nums2, n))