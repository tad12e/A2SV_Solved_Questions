# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        result=0
        ans=0

        def dfs(node, parent, grandparent):
            
            nonlocal ans

            if not node:
                return 0

            if grandparent and grandparent.val %2==0:
                ans+=node.val

            dfs(node.right, node, parent)
            dfs(node.left, node, parent)
        dfs(root, None, None)
        return ans
            







        