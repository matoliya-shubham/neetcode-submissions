# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode):
        if not head:
            return None
        curr = head
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

        # l1_rev = self.reverseList(l1)
        # l2_rev = self.reverseList(l2)
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = num2 = ''
        curr = l1
        while curr:
            num = str(curr.val)
            num1 = num + num1
            curr = curr.next
        curr = l2
        while curr:
            num = str(curr.val)
            num2 = num + num2
            curr = curr.next
        sum = str(int(num1) + int(num2))[::-1]
        head = ListNode(0)
        curr = head
        for num in sum:
            node = ListNode(int(num))
            curr.next = node
            curr = curr.next
        return head.next


