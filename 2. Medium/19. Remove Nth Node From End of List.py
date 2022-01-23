# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = ListNode(0)
        node.next = head

        current = last = node

        for _ in range(n):
            last = last.next

        while last:
            prev = current
            current = current.next
            last = last.next

            if not last:
                prev.next = current.next

        return node.next