class Solution:
    def anagram(self, word1: str, word2: str) -> bool:
        hash_table = [0] * 26
        for c1 in word1:
            hash_table[ord(c1) - ord('a')] += 1
        for c2 in word2:
            hash_table[ord(c2) - ord('a')] -= 1
        for ent in hash_table:
            if ent != 0:
                return False
        return True

Solution().anagram('tree','taar')


