# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return 0

        test = self.lowestCommonAncestor(root.left, p, q)
        if isinstance(test, TreeNode):
            return test

        if root is p or root is q:
            test += 1

        if test < 2:
            temp = self.lowestCommonAncestor(root.right, p, q)
            if isinstance(temp, TreeNode):
                return temp
            test += temp

        if test == 2:
            return root
        else:
            return test
