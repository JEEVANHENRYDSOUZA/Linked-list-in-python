class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prevSlow = ListNode(0, head)
        slow = fast = head
        while fast and fast.next:
            prevSlow = slow
            slow = slow.next
            fast = fast.next.next
        
        prevSlow.next = slow.next
        return dummy.next
