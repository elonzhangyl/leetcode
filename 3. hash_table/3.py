class Solution:
    def intersection(self, lst1: list[int], lst2: list[int]) -> list[int]:
        set1 = set(lst1)
        set2 = set(lst2)
        lst12 = []
        if len(set1) > len(set2):
            temp = set2
            set2 = set1
            set1 = temp
        for s in set1:
            if s in set2:
                lst12.append(s)
        return lst12

Solution().intersection(lst1=[1,2,7],lst2=[2,3,2,7])
