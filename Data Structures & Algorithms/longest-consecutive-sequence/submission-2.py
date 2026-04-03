class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        res = []
        cnt = 0
        for k,v in enumerate(nums):
            if k == len(nums) - 1:
                if v-1 == nums[k-1]:
                    cnt += 1
                    res.append(cnt)
                else:
                    cnt += 1
                    res.append(cnt)
                break
            elif v == nums[k+1]:
                continue
            elif v+1 == nums[k+1]:
                cnt += 1    
            else:
                cnt += 1
                res.append(cnt)
                cnt = 0
        if len(res) == 0:
            return 0
        return max(res)           

