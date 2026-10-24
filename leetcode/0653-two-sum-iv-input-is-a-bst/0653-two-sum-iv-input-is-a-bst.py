# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        li=[]
        if not root:
            return False


        def dfs(node):

            if not node:
                return
            if node.val not in li:
                li.append(node.val)

            dfs(node.right)
            dfs(node.left)
        dfs(root)
        print(li)
        if len(li)<=1:
            return False

        for i in li:
            j=k-i
            if j in li and (j != i or li.count(i) > 1):
                return True
        return False

                   