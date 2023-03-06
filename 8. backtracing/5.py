class Solution:
    def __init__(self):
        self.res = []
        self.path = ''
        self.letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
    def dia(self, digits):
        self.backtracking(digits, 0)
        return self.res

    def backtracking(self, digits, idx):
        if idx >= len(digits):
            self.res.append(self.path[:])
            return

        for letter in self.letter_map[digits[idx]]: # 相当于两层for循环对应不同的nums，以前是相同的
            self.path += letter
            self.backtracking(digits, idx+1)
            self.path = self.path[:-1]

print(Solution().dia('23'))