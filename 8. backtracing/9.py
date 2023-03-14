
class Solution:
    def __init__(self):
        self.res = []
        self.path = []

    def slice_palindrome(self, s):
        self.backtracking(s)
        return self.res

    def backtracking(self, s):
        if len(s) == 0:
            self.res.append(self.path[:])
            return

        for i in range(len(s)):
            if self.is_palindrome(s[:i+1]):
                self.path.append(s[:i+1])
                self.backtracking(s[i+1:])
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