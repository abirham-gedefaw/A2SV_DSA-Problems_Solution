# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # TC = o(D) SC = o(D)
        # if not root:
        #     return None
        # if root.val < val:
        #     return self.searchBST(root.right, val)
        # if root.val > val:
        #     return self.searchBST(root.left, val)
        # return root

        
        # TC = o(D) SC = o(1)
        node = root
        while node:
            if val > node.val: node =  node.right
            elif val < node.val : node = node.left
            else:
                return node
        return node
        