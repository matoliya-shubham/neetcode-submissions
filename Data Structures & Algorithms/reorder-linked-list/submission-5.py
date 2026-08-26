# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle first 
        middle = None
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        prev = None
        curr = second
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        slow.next = None
        # now we have to merge head ad prev
        # prev will always be shorter
        while prev:
            temp1 = head.next
            temp2 = prev.next
            head.next = prev
            prev.next = temp1
            head = temp1
            prev = temp2


        
