class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    

class Solution:
    def addTwoNumbers(self, l1, l2):
        print(l1[::-1])

solution = Solution()
l1 = [2,4,3]
l2 = [5,6,4]
print(solution.addTwoNumbers(l1, l2))