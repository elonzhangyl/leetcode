class Solution:
    def fibonacci(self, n):
        fib = []
        fib[0] = 0
        fib[1] = 1
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            fib
            for n in range(3, n):
                fib[n] = fib[n-1] + fib[n-2]
            return fib[n]