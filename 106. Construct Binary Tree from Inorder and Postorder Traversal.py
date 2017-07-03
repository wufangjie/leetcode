'''
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        n = len(inorder)
        idx = {key: pos for key, pos in zip(inorder, range(n))}

        def build_rec(p1, p2, q1, q2):
            if p2 < p1 and q2 < q1:
                return None
            i = idx[postorder[p2]]
            node = TreeNode(postorder[p2])
            node.left = build_rec(p1, p1 + i - q1 - 1, q1, i - 1)
            node.right = build_rec(p1 + i - q1, p2 - 1, i + 1, q2)
            return node

        return build_rec(0, n - 1, 0, n - 1)
