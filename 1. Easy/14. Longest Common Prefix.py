class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        if not strs: return prefix
        
        for i in range(len(min(strs))):
            c = strs[0][i]
            if all(a[i] == c for a in strs):
                prefix += c
            else:
                break
        return prefix

solution = Solution().longestCommonPrefix(["flower","flow","flight"])
print(solution)

string = '123456'
print(string[2:])