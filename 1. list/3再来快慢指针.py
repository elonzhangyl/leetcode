class Solution:
    def remove(self, nums, target):
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != target:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return nums[0:slow], slow

print(Solution().remove([1,2,3,4], 3))
