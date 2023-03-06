class Solution:
    def reverse_str(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s

print(Solution().reverse_str(["h","e","l","l","o"]))