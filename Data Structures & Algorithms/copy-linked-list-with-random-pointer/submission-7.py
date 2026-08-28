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
        # we need to create a map for this 
        raw_map = {} # old Node, new Node 
        curr = head
        while curr:
            raw_map[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            raw_map[curr].next = raw_map[curr.next] if curr.next else None
            raw_map[curr].random = raw_map[curr.random] if curr.random else None
            curr = curr.next
        
        return raw_map[head]

