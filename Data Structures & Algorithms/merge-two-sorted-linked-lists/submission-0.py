# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return

        dummy = ListNode(-1)
        node = dummy

        while list1 or list2:
            next_node = None

            if list1 and list2:
                if list1.val <= list2.val:
                    next_node = list1
                    list1 = list1.next
                else:
                    next_node = list2
                    list2 = list2.next
            elif list1:
                next_node = list1
                list1 = list1.next
            else:
                next_node = list2
                list2 = list2.next

            node.next = next_node
            node = node.next
        return dummy.next