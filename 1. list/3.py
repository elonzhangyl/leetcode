class Solution:
    def remove(self, nums, target):
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] == target:
                fast += 1
                if fast < len(nums):
                    nums[slow] = nums[fast]
            else:
                nums[slow] = nums[fast]
                fast += 1
                slow += 1
        return nums[:slow]

print(Solution().remove([0,1,2,2,3,0,4,2], 2))
