
class Solution:
    def __init__(self):
        self.res = []
        self.path = []

    def slice_palindrome(self, s):
        self.backtracking(s, 0)
        return self.res

    def backtracking(self, s, start):
        if start >= len(s):
            self.res.append(self.path[:])
            return

        for i in range(start, len(s)):
            if self.is_palindrome(s[start:i+1]):
                self.path.append(s[start:i+1])
                self.backtracking(s, i+1)
                self.path.pop()
    
    def is_palindrome(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

print(Solution().slice_palindrome('aab'))