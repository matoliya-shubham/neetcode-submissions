# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ans = True
        def dfs(p, q):
            nonlocal ans
            if not p and not q:
                return 
            elif p and not q:
                ans = False
                return
            elif q and not p:
                ans = False
                return
            if p and q and p.val != q.val:
                ans = False
            dfs(p.left, q.left)
            dfs(p.right, q.right)
        dfs(p, q)
        return ans 