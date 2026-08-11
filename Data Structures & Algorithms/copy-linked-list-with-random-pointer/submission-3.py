"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None
    
        # 1. Insert copied node after every original node
        curr = head
    
        while curr:
            new_node = Node(curr.val)
    
            new_node.next = curr.next
            curr.next = new_node
    
            curr = new_node.next
    
        # 2. Copy random pointers
        curr = head
    
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
    
            curr = curr.next.next
    
        # 3. Separate original and copied lists
        curr = head
        new_head = head.next
    
        while curr:
            new_node = curr.next
    
            curr.next = new_node.next
    
            if new_node.next:
                new_node.next = new_node.next.next
    
            curr = curr.next
    
        return new_head









