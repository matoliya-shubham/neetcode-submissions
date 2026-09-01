# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root: Optional[TreeNode]):
            nonlocal ans
            if not root:
                return 0
            left_height = dfs(root.left)
            right_height = dfs(root.right)
            curr_dia = left_height + right_height
            ans = max(ans, curr_dia)
            return 1 + max(right_height, left_height)

        dfs(root)
        return ans