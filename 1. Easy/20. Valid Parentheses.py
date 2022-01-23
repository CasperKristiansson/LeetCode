class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for parentheses in s:
            if parentheses in ['(', '[', '{']:
                stack.append(parentheses)
            else:
                parenthese = stack.pop()
                if parentheses == ')' and parenthese != '(' or parentheses == ']' and parenthese != '[' or parentheses == '}' and parenthese != '{':
                    return False

        return not stack

solutuion = Solution().isValid('()[]{}')
print(solutuion)