# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return root
        lca = root #root is common ancester of all nodes
        while lca:
            if (lca.val >= p.val and lca.val <= q.val) or (lca.val >= q.val and lca.val <= p.val):
                return lca
            if p.val < lca.val and q.val < lca.val:
                lca = lca.left
            elif p.val > lca.val and q.val > lca.val:
                lca = lca.right
        return lca