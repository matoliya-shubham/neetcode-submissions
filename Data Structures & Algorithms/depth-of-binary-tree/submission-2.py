# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])
        count = 0
        while q:
            res = []
            for _ in range(len(q)):
                node = q.pop()
                if node and node.left:
                    res.append(node.left)
                if node and node.right:
                    res.append(node.right)
            count += 1
            q = deque(res)
        return count
