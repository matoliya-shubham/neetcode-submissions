# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        sum = root.val
        # we need to think about two things for each node
        # 1. what should that node return to its parent?
        # 2. is this node could be a best path?
        def dfs(root):
            nonlocal sum
            if not root:
                return 0
            # ignore negative values
            leftsum = max(0, dfs(root.left))
            rightsum = max(0, dfs(root.right))
            # to check if this node has best path going through it
            sum = max(sum, root.val + leftsum + rightsum)
            # a node should return best of two paths to its parent 
            return root.val + max(leftsum, rightsum)

        dfs(root)
        return sum

        