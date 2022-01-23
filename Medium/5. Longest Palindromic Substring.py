class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        
        for i in range(len(s)):
            string = s[i]

            for j in range(i + 1, len(s)):
                if s[j] != s[i] or (j + 1 < len(s) and s[j + 1] == s[i]):
                    string += s[j]
                else:
                    string += s[j]
                    break
            
                print(string)
            
            if len(string) > len(result) and string[-1] == s[i]:
                result = string
        
        return result
        