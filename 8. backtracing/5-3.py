class Solution:
    def __init__(self):
        self.i = -1
        self.path = []
        self.res = []

    def dial(self, nums):
        dia = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        letters_list = []
        for num in nums:
            letters_list.append(dia[num])
        self.backtracking(letters_list)

        return self.res

    def backtracking(self, letters_list):
        if self.i == len(letters_list) - 1:
            self.res.append(''.join(self.path[:]))
            return

        for letter in letters_list[self.i]:
            self.path.append(letter)
            self.i += 1
            self.backtracking(letters_list)
            self.i -= 1
            self.path.pop()


print(Solution().dial('23'))
