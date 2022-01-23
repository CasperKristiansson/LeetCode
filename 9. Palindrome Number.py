class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_list = list(str(x))

        return num_list == num_list[::-1]