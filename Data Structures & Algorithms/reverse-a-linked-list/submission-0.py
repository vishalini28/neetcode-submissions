# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            # 1. Bookmark the next node before breaking the link
            temp = curr.next  
            
            # 2. Reverse the current node's pointer
            curr.next = prev  
            
            # 3. Move the 'prev' pointer one step forward
            prev = curr       
            
            # 4. Move the 'curr' pointer one step forward
            curr = temp       
            
        # 'prev' ends up pointing to the new head node
        return prev
