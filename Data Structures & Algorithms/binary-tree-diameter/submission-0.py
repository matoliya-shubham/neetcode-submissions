# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def maxDia(root1: Optional[TreeNode]):
            nonlocal ans
            if not root1:
                return 0

            left_height = maxDia(root1.left)
            right_height = maxDia(root1.right)
            ans = max(ans, (left_height+right_height))
            return 1+ max(left_height, right_height)
        maxDia(root)
        return ans 
        

        