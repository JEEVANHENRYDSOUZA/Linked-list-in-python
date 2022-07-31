# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def pairSum(self, head: Optional[ListNode]) -> int:
		l=[]
		def recpal(head,l):
			if head is None:
				return []
			else:
				l.append(head.val)
				return recpal(head.next,l)

		recpal(head,l)

		s=set()
		for i in range(len(l)//2):
			 s.add(l[i]+l[~i])

		return max(s)
