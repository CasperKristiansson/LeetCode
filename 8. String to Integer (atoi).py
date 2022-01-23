class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        result = ''

        while i < len(s) and s[i] == ' ':
            i += 1

        if i < len(s):
            if s[i] == '-':
                result += s[i]
                i += 1
            elif s[i] == '+':
                i += 1

        while i < len(s) and s[i].isdigit():
            result += s[i]
            i += 1

        if result in {'-', '+', ''}:
            result = 0

        if int(result) >= 2147483647:
            result = 2147483647
        elif int(result) <= -2147483648:
            result = -2147483648

        return int(result)