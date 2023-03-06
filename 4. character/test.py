class Solution:
    def strStr(self, s: str, p: str) -> int:
        for i in range(len(s)):
            j = 0
            for j in range(len(p)):
                if s[i] == p[j]:
                    i += 1
                    j += 1
                else:
                    break
                if j == len(p):
                    return i - j

            i -= j - 1
            if i == len(s):
                return -1

s = 'BBC ABCDAB ABCDABCDABDE'
p = 'ABCDABD'
Solution().strStr(s, p)