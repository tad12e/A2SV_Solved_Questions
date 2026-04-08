class Solution:
    def deleteNode(self, root, key):

        if not root:
            return None

        # Search for node
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            # Node found

            # Case 1: No left child
            if not root.left:
                return root.right

            # Case 2: No right child
            if not root.right:
                return root.left

            # Case 3: Two children
            minNode = root.right
            while minNode.left:
                minNode = minNode.left

            root.val = minNode.val
            root.right = self.deleteNode(root.right, minNode.val)

        return root

        