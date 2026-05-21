class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in range(len(nums1)):
            idx = nums2.index(nums1[i])
            for num in nums2[idx+1:]:
                if num > nums1[i]:
                    res.append(num)
                    break
            else:
                res.append(-1)
        return res
