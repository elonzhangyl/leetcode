class Solution:
    def replace_blank(self, s):
        s = list(s)
        s_old = len(s) - 1
        c = 0
        for s_ in s:
            if s_ == ' ':
                c += 1
        s = s + [' '] * (c * 2)
        pointer_new = len(s) - 1

        for pointer_old in range(s_old, -1, -1):
            if s[pointer_old] == ' ':
                s[pointer_new - 2: pointer_new + 1] = list('%20')
                pointer_new -= 3
            else:
                s[pointer_new] = s[pointer_old]
                pointer_new -= 1
        return ''.join(s)

print(Solution().replace_blank("We are happy."))

# 输出："We%20are%20happy."