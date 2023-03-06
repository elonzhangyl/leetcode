# 准确理解题意，不要搞多余的功能，复杂了
class Solution:
    def iscolatingList(self, lst: list) -> list:
        count = 1
        pre_d = 0

        for i in range(len(lst) - 1):
            cur_d = lst[i + 1] - lst[i]
            if cur_d * pre_d <= 0 and cur_d != 0:
                count += 1
                pre_d = cur_d
        return count

       
Solution().iscolatingList([1,17,5,10,13,15,10,5,16,8])