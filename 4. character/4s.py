class Solution:
    def removeHeadAndTailSpaces(self, s: str) -> str:
        left, right = 0, len(s) - 1
        while left <= right and s[left] == ' ':
            left += 1
        while left < right and s[right] == ' ':
            right -= 1
        
        temp = []
        while left <= right:
            if s[left] == ' ' and s[left - 1] == ' ':
                pass
            else:
                temp.append(s[left])
            left += 1
        return temp

    def reverseCharacters(self, char1: list[str]) -> list[str]:
        left, right = 0, len(char1) - 1
        while left < right:
            char1[left], char1[right] = char1[right], char1[left]
            left += 1
            right -= 1
        return char1

    def reservesCharactersInWords(self, char1: list[str]) -> list[str]:
        start, seg = 0, 0
        while start + seg < len(char1):
            while start + seg != len(char1) and char1[start + seg] != ' ':
                seg += 1
            char1[start:start+seg] = self.reverseCharacters(char1[start:start+seg])
            start += seg + 1
            seg = 0
        return char1

    def reverse_string(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return None
	    
    def reverse_each_word(self, nums):
        start = 0
        end = 0
        n = len(nums)
        while start < n:
            while end < n and nums[end] != ' ':
                end += 1
            self.reverse_string(nums, start, end-1)
            start = end + 1
            end += 1
        return None

s= "  hello     world!"
s_no_space = Solution().removeHeadAndTailSpaces(s)
s_reverse = Solution().reverseCharacters(s_no_space)
ss = Solution().reservesCharactersInWords(s_reverse)
s_reverse = ''.join(s_reverse)
print(s_reverse)