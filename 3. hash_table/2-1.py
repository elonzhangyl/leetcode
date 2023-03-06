class Solution:
    def __init__(self):
        pass

    def is_(self, s, t):
        record = [0] * 26
        for i in s:
            record[ord(i) - ord('a')] = 1
        for i in t:
            record[ord(i) - ord('a')] = 0
        
        if sum(record) == 0:
            return True
        else:
            return False


print(Solution().is_(s = "anagram", t = "nagaram" ))