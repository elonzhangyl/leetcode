class Solution:
    def binary_search(self, nums, target):
        left, right = 0,  len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid

print(Solution().binary_search([1,2,3], 3))