class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        i, j = 0, 0
        
        while abs(dividend) >= j:
            j += abs(divisor)
            i += 1
            
        if i > 2**31 - 1:
            i = 2**31 - 1
        elif i < -2**31:
            i = -2**31
        
        if (divisor < 0 and dividend < 0) or (divisor >= 0 and dividend >= 0):
            return i - 1
        else:
            return -i + 1

solution = Solution().divide(-2147483648, -1)
print(solution)