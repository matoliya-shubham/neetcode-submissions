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
        # we create a new node next to each node which will be copy of that and link them all finally
        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = curr.next.next
        curr = head
        # copy random nodes
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        curr = head 
        copy = curr.next
        while curr:
            new_node = curr.next
            curr.next = new_node.next
            if new_node.next:
                new_node.next = new_node.next.next
            curr = curr.next
        return copy
