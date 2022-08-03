# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = prev = head
        cur = cur.next
        
        while cur:
            _next = cur.next
            
            if cur.val < 0:
                prev.next = _next
                cur.next = head
                head = cur
            else:
                prev = cur
            
            cur = _next
        
        return head
