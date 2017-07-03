'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree_TLE(self, preorder, inorder):
        if not preorder:
            return None
        for i, elem in enumerate(inorder):
            if elem == preorder[0]:
                break
        node = TreeNode(preorder[0])
        node.left = self.buildTree(preorder[1:i + 1], inorder[:i])
        node.right = self.buildTree(preorder[i + 1:], inorder[i + 1:])
        return node


    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        n = len(inorder)
        idx = {key: pos for key, pos in zip(inorder, range(n))}

        def build_rec(p1, p2, q1, q2):
            if p2 < p1 and q2 < q1:
                return None
            i = idx[preorder[p1]]
            node = TreeNode(preorder[p1])
            node.left = build_rec(p1 + 1, p1 + i - q1, q1, i - 1)
            node.right = build_rec(p1 + i - q1 + 1, p2, i + 1, q2)
            return node

        return build_rec(0, n - 1, 0, n - 1)
