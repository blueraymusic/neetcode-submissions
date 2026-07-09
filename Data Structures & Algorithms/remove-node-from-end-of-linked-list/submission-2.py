# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy.next
        count = 0 

        while fast:
            fast = fast.next
            count += 1 

            if count >= n+1:
                slow= slow.next
            
        slow.next = slow.next.next

        return dummy.next