class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            return TreeNode(val)

        def dfs(node):
            if val > node.val:
                if node.right is None:
                    node.right = TreeNode(val)
                else:
                    dfs(node.right)
            else:
                if node.left is None:
                    node.left = TreeNode(val)
                else:
                    dfs(node.left)

        dfs(root)
        return root
            

        