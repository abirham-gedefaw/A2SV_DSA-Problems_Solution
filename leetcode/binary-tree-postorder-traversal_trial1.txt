# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def post_traversal(node):
            if not node:
                return
            post_traversal(node.left)
            post_traversal(node.right)
            result.append(node.val)
        post_traversal(root) 
        return result      
        