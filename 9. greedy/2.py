class Solution:
    def cookies(self, g, s):
        idx = 0
        c = 0
        for i in range(len(s)-1, -1, -1):
            if idx < len(g) and s[i] >= g[idx]:
                c += 1
                idx += 1
        return c
print(Solution().cookies(g = [1,2], s = [1,2,3]))
