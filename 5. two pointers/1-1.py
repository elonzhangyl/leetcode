# 1. 额外空间，内存不够时怎么办
# 2. 使用append，list空间一直变化，会导致额外的复制操作
class Solution:
    def remove_element(self, nums, target):
        res = []
        for i in range(len(nums)):
            if nums[i] != target:
                res.append(nums[i])
        
        return res

print(Solution().remove_element([0,1,2,2,3,0,4,2], 2))