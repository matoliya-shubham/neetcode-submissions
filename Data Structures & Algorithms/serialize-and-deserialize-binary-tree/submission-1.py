# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        result = []
        q = deque([root])
        while q:
            node = q.popleft()
            if not node:
                result.append("null")
                continue
            result.append(str(node.val))
            q.append(node.left)
            q.append(node.right)

        return ','.join(result)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        # 1,2,null,null,3,4,null,null,5,null,null
        res = data.split(',')
        root = TreeNode(int(res[0]))
        index = 1
        q = deque([root])
        while q:
            node = q.popleft()
            if res[index] != "null":
                node.left = TreeNode(int(res[index]))
                q.append(node.left)
            index += 1
            if res[index] != "null":
                node.right = TreeNode(int(res[index]))
                q.append(node.right)
            index += 1
        return root


        













