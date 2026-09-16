"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        # Step 1: Create a dictionary to pair (Old Node -> New Node)
        clones = {None: None}

        # Step 2: Make a new copy of every node's value
        curr = head
        while curr:
            clones[curr] = Node(curr.val)
            curr = curr.next

        # Step 3: Copy the connections (arrows)
        curr = head
        while curr:
            clones[curr].next = clones[curr.next]
            clones[curr].random = clones[curr.random]
            curr = curr.next

        # Return the copy of the very first node
        return clones[head]
