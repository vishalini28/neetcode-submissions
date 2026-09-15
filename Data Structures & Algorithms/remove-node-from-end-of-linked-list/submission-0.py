# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes=[]
        curr=head
        while curr:
            nodes.append(curr)
            curr=curr.next
        total=len(nodes)
        if total==n:
            return head.next
        before=total-n-1
        nodes[before].next=nodes[before].next.next
        return head
    
        