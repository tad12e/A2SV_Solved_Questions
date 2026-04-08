# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root==None:
            return TreeNode(val)


        def dfs(node, val):



            if val>node.val:
                if node.right is None:
                   node.right=TreeNode(val)

                else:dfs(node.right, val)
            else:
                if node.left is None:
                   node.left=TreeNode(val)
                else:dfs(node.left, val)
        dfs(root, val)

        return root


        
        