# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head is None and head.next is None):
            return None#checking for empty linked list
        
        
        current= head
        prev=None
        while(current is not None ):
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
            
            
        return prev#new head of the revrsed linked list
            
            
            
