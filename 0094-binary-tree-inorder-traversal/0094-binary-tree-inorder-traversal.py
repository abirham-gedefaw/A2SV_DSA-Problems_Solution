# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # result = []
        # def inorder_traversal(node):
        #     if node is not None:
        #         inorder_traversal(node.left)
        #         result.append(node.val)
        #         inorder_traversal(node.right)
        # inorder_traversal(root)
        # return result

        cur, stack = root, []
        result = []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            result.append(cur.val)
            cur = cur.right
        return result

