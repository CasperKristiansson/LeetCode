class Solution:
    def reverse(self, x: int) -> int:
        num = [str(i) for i in str(x)]
        
        while len(num) > 1 and num[-1] == '0':
            del num[-1]
        
        if(num[0] == "-"):
            del num[0]
            num.append('-')
        
        num = int(''.join(num[::-1]))

        
        if abs(num) >= 2147483648:
            num = 0
        
        return num