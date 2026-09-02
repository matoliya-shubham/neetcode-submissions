# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        stack = []
        curr = root
        last_visited = None
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            peak = stack[-1]
            if last_visited == peak.right or not peak.right:
                node = stack.pop()
                last_visited = node
                res.append(node.val)
                curr = None
            else:
                curr = peak.right
        return res
        