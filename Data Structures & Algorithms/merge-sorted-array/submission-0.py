class Solution:
    def merge(self, nums1, m, nums2, n):
        j = 0

        for i in range(len(nums1)):
            if nums1[i] == 0:
                nums1[i] = nums2[j]
                j += 1

        nums1.sort()


        """
        Do not return anything, modify nums1 in-place instead.
        """
        