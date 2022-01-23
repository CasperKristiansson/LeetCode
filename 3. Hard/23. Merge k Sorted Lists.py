class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        def mergeTwoLists(list1, list2):
            node = result = ListNode(0)
            
            while list1 and list2:
                if list1.val < list2.val:
                    node.next = list1
                    list1 = list1.next
                else:
                    node.next = list2
                    list2 = list2.next
                    
                node = node.next
            
            while list1:
                node.next = list1
                node = node.next
                list1 = list1.next
            
            while list2:
                node.next = list2
                node = node.next
                list2 = list2.next
            
            return result.next
        
        if len(lists) == 3:
            merged = mergeTwoLists(lists[0], lists[1])
            return mergeTwoLists(merged, lists[2])
        elif len(lists) == 2:
            return mergeTwoLists(lists[0], lists[1])
        elif len(lists) == 1:
            return lists[0]
        else:
            return lists

solution = Solution().mergeKLists([ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))])
while solution:
    print(solution.val)
    solution = solution.next