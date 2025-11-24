class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        

        i = 0 #1
        j = 0 #2
        len1 = len(nums1)
        len2 = len(nums2)

        merged = []

        while(i < len1 and j < len2):
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        while (i < len1):
            merged.append(nums1[i])
            i += 1

        while (j < len2):
            merged.append(nums2[j])
            j += 1

        len_merged = len(merged)
        if len_merged % 2 == 0:
            return (merged[len_merged//2 - 1] + merged[len_merged//2]) / 2.0
        else:
            return merged[len_merged//2]
