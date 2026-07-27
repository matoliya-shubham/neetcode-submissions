# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        stack = []
        curr = root
        last_visited = None
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            # now access top of stack
            peak = stack[-1]
            # now we will visit this peak node if this node doesn't have right node 
            # OR right node is already visited node else curr = curr.right
            if not peak.right or last_visited == peak.right:
                node = stack.pop()
                res.append(node.val)
                last_visited = node
                curr = None
            else:
                curr = peak.right
        return res

                
        