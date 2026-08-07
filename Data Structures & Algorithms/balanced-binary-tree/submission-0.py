# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = True
        def isBal(root: Optional[TreeNode]):
            nonlocal ans
            if not root:
                return 0

            left_height = isBal(root.left)
            right_height = isBal(root.right)
            if abs(left_height - right_height) > 1:
                ans = False
            return 1 + max(left_height, right_height)
        isBal(root)
        return ans
        