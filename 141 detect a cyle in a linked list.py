lass Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if(head is  None ):
            return None
        slow=head
        fast=head
        while(fast is not None and fast.next.next is not None):
            if(slow==fast):
                return True
            slow=slow.next
            fast=fast.next.next
            
        return False
