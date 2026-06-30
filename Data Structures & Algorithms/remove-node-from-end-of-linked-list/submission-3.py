# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
   def removeNthFromEnd(self, head, n):
    # step 1 — reverse list
    curr, prev = head, None
    while curr:
        temp = curr.next
        curr.next = prev    # reverse arrow
        prev = curr
        curr = temp         # ✅ just move forward

    # step 2 — remove nth node (now nth from start)
    prev_node = None
    p = prev
    i = 1
    while i < n:
        prev_node = p
        p = p.next
        i += 1

    if not prev_node:
        prev = prev.next    # ✅ skip head
    else:
        prev_node.next = prev_node.next.next

    # step 3 — reverse back
    curr, pre = prev, None
    while curr:
        temp = curr.next
        curr.next = pre     # reverse arrow
        pre = curr
        curr = temp         # ✅ just move forward

    return pre


