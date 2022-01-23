class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(s) > len(p):
            return False

        return not any(
            (
                p[i] != '*'
                or s[i] not in p[:i + 1]
                and '.' not in p[:i + 1]
            )
            and p[i] != s[i]
            and p[i] != '.'
            for i in range(len(s))
        )
