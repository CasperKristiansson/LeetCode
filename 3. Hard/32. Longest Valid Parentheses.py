class Solution:
    def longestValidParentheses(self, s: str) -> int:
        counter, i, result = 0, 0, 0
        stack = []

        while i < len(s):
            if s[i] in ['(', '[', '{']:
                stack.append(s[i])
            elif not stack:
                if counter > result:
                    result = counter
                counter = 0
            else:
                para = stack.pop()
                if s[i] == ')' and para == '(' or s[i] == ']' and para == '[' or s[i] == '}' and para == '{':
                    counter += 2
                else:
                    stack = []
                    if counter > result:
                        result = counter
                    counter = 0

            i += 1

        if counter - len(stack) > result:
            result = counter

        return result
    
    def simple(self, s: str) -> int:
        stack = [0,]
        max_parenthesis = 0
        for bracket in s:
            if bracket == '(':
                stack.append(0)
            elif len(stack) > 1:
                val = stack.pop()
                stack[-1] += val + 2
                max_parenthesis = max(max_parenthesis, stack[-1])
            else:
                stack = [0]

        return max_parenthesis
                
solution = Solution().longestValidParentheses('(()()()((()')
print(solution)