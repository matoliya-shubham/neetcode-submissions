# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ans = None
        def dfs(root, p, q):
            nonlocal ans
            if not root:
                return None
            if (p.val <= root.val <= q.val) or (q.val <= root.val <= p.val):
                ans = root
            elif p.val < root.val and q.val < root.val:
                dfs(root.left, p, q)
            else:
                dfs(root.right, p, q)
        dfs(root, p, q)
        return ans 
        