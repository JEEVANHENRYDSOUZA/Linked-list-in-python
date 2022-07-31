# Time and space = O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        # hold the count of each node
        count = self.countOccurance(head)
        # print(count)
        
        # create a sentinel node
        dummy = ListNode()
        prev_node = dummy
        prev_node.next = head
        
        cur_node = head
        
        while cur_node:
            # check if it has occured only once. If yes then just move the pointer
            if count[cur_node.val] == 1:
                prev_node = cur_node
                cur_node = cur_node.next
            else:
                # the node appeared more than once
                while cur_node and count[cur_node.val] != 1:
                    cur_node = cur_node.next
                
                prev_node.next = cur_node
                
        return dummy.next
        
        
    
    def countOccurance(self, head):
        dic = {}
        
        cur_node = head
        
        while cur_node:
            # initializing
            if cur_node.val not in dic:
                dic[cur_node.val] = 0
            
            dic[cur_node.val] += 1
            
            cur_node = cur_node.next
        

        return dic
      
      
      
#remove all the oucurances of that node which is duplicate
