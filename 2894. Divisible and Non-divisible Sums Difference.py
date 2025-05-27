class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        nums1, nums2 = 0, 0
        i = 1
        for i in range(n+1):
            if (i % m == 0):
                nums2 += i
            else:
                nums1 += i

        return (nums1 - nums2)