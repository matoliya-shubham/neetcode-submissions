# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
   def removeNthFromEnd(self, head, n):
    # step1: reverse list
    # step2: get node just before next and change its next pointer to next.next
    # step3: again reverse list

    # reverse list
    prev, curr = None, head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    p = prev # reversed list
    prev_node = None
    i = 1
    while i < n:
        prev_node = p
        p = p.next
        i += 1
    
    # change next pointer of node before n
    if not prev_node:
        prev = prev.next
    else:
        prev_node.next = prev_node.next.next

    # reverse list again 
    pre, curr = None, prev
    while curr:
        next_node = curr.next
        curr.next = pre
        pre = curr
        curr = next_node
    return pre

