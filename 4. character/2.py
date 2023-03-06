class Solution:
    def reverseStr(self, s: list[str]) -> list:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s

    def reserveStr2(self, s: str, k: int) -> str:
        ss = list(s)
        for cur in range(0, len(s), 2*k):
            ss[cur: cur+k] = self.reverseStr(ss[cur: cur+k])

        return ''.join(ss)

# 输入: s = "abcdefg", k = 2
# 输出: "bacdfeg"
print(Solution().reserveStr2('abcdefg', 2))
#
