# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder, postorder):

        def build(pre, post):
            if not pre:
                return None

            root = TreeNode(pre[0])

            if len(pre) == 1:
                return root

            left_root = pre[1]

            index = post.index(left_root)

            left_size = index + 1

            root.left = build(
                pre[1:left_size + 1],
                post[:left_size]
            )

            root.right = build(
                pre[left_size + 1:],
                post[left_size:-1]
            )

            return root

        return build(preorder, postorder)
            




        


        