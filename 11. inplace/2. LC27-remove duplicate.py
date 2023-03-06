# 示例 2: 给定 nums = [0,1,2,2,3,0,4,2], val = 2, 
# 函数应该返回新的长度 5, 
# 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。

class Solution:
    def remove_duplicates(self, nums, val):
        i, j = 0, 0
        while j < len(nums):
            if nums[i] == val:
                j += 1
                nums[i] = nums[j]
            if nums[i] != val:
                i += 1
                j += 1
        return nums  

print(Solution().remove_duplicates([0,1,2,2,3,0,4,2], 2))            