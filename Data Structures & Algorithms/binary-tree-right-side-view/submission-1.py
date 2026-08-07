# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    from collections import deque
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque()
        q.append(root)
        res = []
        while q:
            temp = []
            for _ in range(len(q)):
                node = None
                if(len(q) == 1):
                    node = q.popleft()
                    res.append(node.val)
                else:
                    node = q.popleft()
                if(node.left):
                    temp.append(node.left)
                if(node.right):
                    temp.append(node.right)
            for node in temp:
                q.append(node)
        return res
