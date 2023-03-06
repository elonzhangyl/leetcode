class Solution():
    def splitNumber(self, num: int) -> list:
        digits = []
        while num != 0:
            digits.append((num % 10))
            num = num//10
        return digits

    def isHappyNumber(self, num: int) -> bool:
        
        record = set()
        while True:
            digit_square_sum = 0
            digits = self.splitNumber(num)
            digit_square_sum = sum([digit**2 for digit in digits])
            num = digit_square_sum

            if digit_square_sum == 1:
                return True
            if digit_square_sum in record:
                return False
            record.add(digit_square_sum)

Solution().isHappyNumber(189)
