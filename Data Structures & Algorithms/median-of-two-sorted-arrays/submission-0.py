class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        length = len(nums1)
        mid = length // 2
        if length % 2:
            return float(nums1[mid])
        else:
            res = (nums1[mid] + nums1[mid-1]) / 2
            return res
