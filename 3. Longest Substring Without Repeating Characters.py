class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        for i in range(len(s)):
            result = [s[i]]
            for j in range(i + 1, len(s)):
                if s[j] not in result:
                    result.append(s[j])
                else:
                    break
            if len(result) > length:
                length = len(result)
        
        return length