# 移除空格
class Solution:
    def remove_blank_space(self, s):
        k = 0
        left, right = 0, len(s) - 1
        while left < right and s[left] == ' ':
            left += 1
        while left < right and s[right] == ' ':
            right -= 1
        for i in range(left, right + 1):
            if s[i] == ' ' and s[i - 1] == ' ':
                continue
            s[k] = s[i]
            k += 1
        return s[0:k]

    def reverse_str(self, s, left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s

    def reverse_word(self, s):
        s = list(s)
        s = self.remove_blank_space(s)
        s = self.reverse_str(s, 0, len(s) -1)
        start, end = 0, 0
        while start < len(s):                
            while end < len(s) and s[end] != ' ':
                end += 1
            s = self.reverse_str(s, start, end - 1)
            start = end + 1
            end += 1

        return ''.join(s)


print(Solution().reverse_word("  the sky  is blue !  "))