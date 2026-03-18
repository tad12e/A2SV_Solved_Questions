# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # parent, explore left, explore right

        # order = [1, 2, 4, 5, 6, 7, 3, 8, 9]
        order = []

        # append current root to order
        # explore left subtree
        # explore right subtree

        def dfs(node):
            if not node:
                return
            order.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        
        return order