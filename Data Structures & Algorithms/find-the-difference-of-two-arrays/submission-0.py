class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        res = []
        first = list(nums1.difference(nums2))
        second = list(nums2.difference(nums1))
        res.append(first)
        res.append(second)
        return res