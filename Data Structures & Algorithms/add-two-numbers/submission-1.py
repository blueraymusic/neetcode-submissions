# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        hold = 0
        dummy = ListNode(0)
        d = dummy

        while l1 or l2 or hold:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            t = val1 + val2 + hold
            r = t % 10
            hold = t // 10

            d.next = ListNode(r)
            d = d.next

            if l1:
                l1 = l1.next
            
            if l2:
                l2 = l2.next
        
        return dummy.next