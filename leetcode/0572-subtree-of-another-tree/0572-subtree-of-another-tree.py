class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:

        def dfs(node, node2):

            if node is None:
                return False

            if node.val == node2.val:
                if check(node, node2):
                    return True

            if dfs(node.left, node2):
                return True

            if dfs(node.right, node2):
                return True

            return False

        def check(node1, node2):

            if node1 is None and node2 is None:
                return True

            if node1 is None or node2 is None:
                return False

            if node1.val != node2.val:
                return False

            return check(node1.left, node2.left) and check(node1.right, node2.right)

        if subRoot is None:
            return True

        return dfs(root, subRoot)