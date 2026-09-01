# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        curr = root
        last_visited = None
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            peak = stack[-1]
            if peak.right == last_visited or not peak.right:
                node = stack.pop()
                res.append(node.val)
                last_visited = node
                curr = None
            else:
                curr = peak.right
        return res
