# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        final = float("inf")
        depth = 0

        def dfs(node):
            nonlocal depth, final  # Declared inside the inner function

            depth += 1

            # Leaf node check
            if not node.left and not node.right:
                final = min(final, depth)

            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

            # Backtrack when exiting this node
            depth -= 1

        dfs(root)
        return final