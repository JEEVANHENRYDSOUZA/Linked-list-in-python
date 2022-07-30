# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        
        current=head
        temp=head
        while(current is not None):
            count_m_nodes=m
            count_n_nodes=n
            
            while(current is not None and count_m_nodes!=0):
                temp=current
                current=current.next
                count_m_nodes-=1
                

            
            while(current is not None and count_n_nodes!=0):
                current=current.next
                count_n_nodes-=1
            
          
           
            temp.next=current

            
        
        return head   
        
                        
    
                
        
