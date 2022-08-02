# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        current=head.next
        current_sum=0
        while(current is not None):
            if(current.val==0):
                if(prev is None):
                    prev=head#intially prev will be none hence making it point to the start of the linked list
                else:
                    prev=prev.next
                prev.val=current_sum#thwe modified node will be the prev node
                current_sum=0
            else:
                current_sum=current_sum+current.val
            current=current.next#traversal moving current ahead
        
        prev.next=None#removing the links
        return head
        #the head of the returned list should directlty point to the changed element
        
