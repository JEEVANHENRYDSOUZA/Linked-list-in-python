# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head
        prev=None
        curr=head
        last=None
        rev_end=None
        group_count=0
        while curr is not None:
            rev_end=curr
            last=prev
            count=0
            while curr is not None and count<group_count+1:
                prev=curr
                curr=curr.next
                count+=1
            if count%2==0:
                last.next=self.reverse(rev_end,curr)
                rev_end.next=curr
                prev=rev_end
                
            group_count+=1
        return head
            
    def reverse(self,head,until):
        prev2=None
        p2=head

        while p2!=until:
            q2=p2.next
            p2.next=prev2
            prev2=p2
            p2=q2
        return prev2
