
class Solution:
    def __init__(self):
        self.res = []
        self.path = []

    def ip(self, s):
        self.backtracking(s, 0)
        return self.res

    def backtracking(self, s, start):
        if start == len(s) and len(self.path) == 4:
            self.res.append(self.path[:])
            return

        for i in range(start, len(s)):
            cur = s[start:i+1]
            if len(cur) == 1 or \
                (len(cur)>1 and 1 <= int(cur) <= 255):
                self.path.append(s[start:i+1])
                self.backtracking(s, i+1)
                self.path.pop()


print(Solution().ip("25525511135"))