class Solution:
    def __init__(self):
        pass

    def happy_num(self, num):
        sum_ = set()
        while len(sum_) > 1 and sum_[-1] != 1:
            nn = self.sq_digit(num)
            sum_.add(nn)
            if nn in sum_:
                return 0
        
        return 1

    def sq_digit(self, num):
        digit_sum = 0
        while num != 0:
            digit_sum += (num % 10)**2
            num = num // 10
        return digit_sum

print(Solution().happy_num(189))
