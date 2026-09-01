# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = True
        def dfs(root):
            nonlocal ans
            if not root:
                return 0
            h_left = dfs(root.left)
            h_right = dfs(root.right)
            if abs(h_left - h_right) > 1:
                ans = False
            return 1 + max(h_left, h_right)
        dfs(root)
        return ans