class Solution:
    def canConstruct(self, str1: str, str2: str) -> bool:
        def str2dic(str1):
            dict1 = {}
            for s in str1:
                if s in dict1:
                    dict1[s] += 1
                else:
                    dict1[s] = 1
            return dict1

        dict1 = str2dic(str1)
        dict2 = str2dic(str2)

        for d in dict1:
            if d not in dict2 or dict1[d] > dict2[d]:
                return False
        return True

Solution().canConstruct("aa", "ab")


